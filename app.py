import io
import json
import re
from pathlib import Path

import pandas as pd
import streamlit as st
from textblob import TextBlob


st.set_page_config(
    page_title="Signal / Sentiment",
    page_icon="S",
    layout="wide",
)


SUPPORTED_TYPES = ["txt", "md", "log", "csv", "tsv", "json", "xlsx", "xls", "pdf", "docx"]


def clean_text(text):
    text = str(text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    return re.sub(r"\s+", " ", text.replace("RT", "").strip())


def sentiment_category(polarity):
    if polarity > 0.05:
        return "Positive"
    if polarity < -0.05:
        return "Negative"
    return "Neutral"


def json_strings(value):
    if isinstance(value, dict):
        for item in value.values():
            yield from json_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from json_strings(item)
    elif value is not None:
        yield str(value)


def extract_text(uploaded_file):
    extension = Path(uploaded_file.name).suffix.lower().lstrip(".")
    raw = uploaded_file.getvalue()

    if extension in {"txt", "md", "log"}:
        text = raw.decode("utf-8", errors="replace")
        return [line for line in text.splitlines() if line.strip()]
    if extension in {"csv", "tsv"}:
        separator = "\t" if extension == "tsv" else ","
        frame = pd.read_csv(io.BytesIO(raw), sep=separator, encoding_errors="replace")
        return frame.fillna("").astype(str).agg(" ".join, axis=1).tolist()
    if extension == "json":
        return list(json_strings(json.loads(raw.decode("utf-8", errors="replace"))))
    if extension in {"xlsx", "xls"}:
        sheets = pd.read_excel(io.BytesIO(raw), sheet_name=None)
        return [
            row
            for frame in sheets.values()
            for row in frame.fillna("").astype(str).agg(" ".join, axis=1).tolist()
        ]
    if extension == "pdf":
        from pypdf import PdfReader

        return [page.extract_text() or "" for page in PdfReader(io.BytesIO(raw)).pages]
    if extension == "docx":
        from docx import Document

        return [paragraph.text for paragraph in Document(io.BytesIO(raw)).paragraphs]
    raise ValueError(f".{extension or 'unknown'} files are not supported yet")


def analyze_file(uploaded_file):
    rows = extract_text(uploaded_file)
    rows = [clean_text(row) for row in rows if clean_text(row)]
    results = []
    for row in rows:
        polarity = TextBlob(row).sentiment.polarity
        results.append({"Text": row, "Polarity": polarity, "Sentiment": sentiment_category(polarity)})
    return pd.DataFrame(results)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    :root { --ink: #17201d; --mint: #dcefe6; --coral: #f16a52; --paper: #f5f2eb; }
    .stApp { background: var(--paper); color: var(--ink); }
    h1, h2, h3, p, label, .stMarkdown { font-family: 'Space Grotesk', sans-serif; }
    h1 { font-size: clamp(2.5rem, 6vw, 5.5rem); line-height: .95; letter-spacing: -0.04em; }
    .eyebrow { color: var(--coral); font: 500 0.75rem 'DM Mono', monospace; letter-spacing: .12em; text-transform: uppercase; }
    .lede { max-width: 650px; font-size: 1.15rem; color: #52605a; }
    .metric { background: var(--mint); padding: 1.2rem; border-left: 4px solid var(--coral); }
    .metric small { display: block; font: 500 .72rem 'DM Mono', monospace; text-transform: uppercase; }
    .metric strong { display: block; margin-top: .4rem; font-size: 2rem; }
    [data-testid="stFileUploader"] { border: 1px dashed #799289; background: rgba(220,239,230,.45); }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="eyebrow">TEXT / SIGNAL / 01</div>', unsafe_allow_html=True)
st.title("Find the feeling\nin your files.")
st.markdown(
    '<p class="lede">Drop in text, tables, documents, or reports. Signal turns readable content into a simple positive, neutral, or negative read.</p>',
    unsafe_allow_html=True,
)
st.divider()

uploads = st.file_uploader(
    "Upload one or more files",
    type=SUPPORTED_TYPES,
    accept_multiple_files=True,
    help="Supported: TXT, Markdown, CSV, TSV, JSON, Excel, PDF, and Word documents.",
)

if not uploads:
    st.info("Upload a file to see its sentiment breakdown.")
else:
    all_results = []
    for uploaded_file in uploads:
        try:
            result = analyze_file(uploaded_file)
            result.insert(0, "File", uploaded_file.name)
            all_results.append(result)
        except Exception as error:
            st.error(f"Could not read {uploaded_file.name}: {error}")

    if all_results:
        results = pd.concat(all_results, ignore_index=True)
        counts = results["Sentiment"].value_counts()
        total = len(results)
        positive = counts.get("Positive", 0)
        neutral = counts.get("Neutral", 0)
        negative = counts.get("Negative", 0)

        st.subheader("Overall read")
        columns = st.columns(4)
        for column, label, value, color in [
            (columns[0], "Items analyzed", total, "#17201d"),
            (columns[1], "Positive", positive, "#238b68"),
            (columns[2], "Neutral", neutral, "#8c7045"),
            (columns[3], "Negative", negative, "#d4513d"),
        ]:
            column.markdown(
                f'<div class="metric"><small>{label}</small><strong style="color:{color}">{value}</strong></div>',
                unsafe_allow_html=True,
            )

        st.subheader("Breakdown")
        chart_data = pd.DataFrame({"Count": counts}).reindex(["Positive", "Neutral", "Negative"]).fillna(0)
        st.bar_chart(chart_data, color="#f16a52")
        st.dataframe(results, use_container_width=True, hide_index=True)