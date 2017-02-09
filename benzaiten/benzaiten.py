#!/usr/bin/env python
import click
from benzaiten.summarization import TextRankSummarizer

@click.command()
@click.argument('source', type=click.File(mode='r', encoding='utf-8'))
@click.argument('target', type=click.File(mode='w', encoding='utf-8'))
def bensum(source, target):
    """Benzaiten Summarizer Help System

    Benzaiten is a tool for automatic text summarization.
    """
    text = source.read()
    summarizer = TextRankSummarizer()
    target.write(summarizer.summarize(text))
