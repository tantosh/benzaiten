#!/usr/bin/env python
import click
from benzaiten.summarization import TextRankSummarizer

@click.command()
@click.argument('source', type=click.File(mode='r', encoding='utf-8'))
@click.argument('target', type=click.File(mode='w', encoding='utf-8'))
@click.option('--sent', default=10)
def bensum(source, target, sent):
    """Benzaiten Summarizer Help System

    Benzaiten is a tool for automatic text summarization.
    """
    text = source.read()
    summarizer = TextRankSummarizer(sent)
    target.write(summarizer.summarize(text))
