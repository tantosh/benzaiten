from summarization import TextRankSummarizer

def main():
    summarizer = TextRankSummarizer()
    path_to_file = ".\\tests\\tests_files\\"
    file_name = "AmericanSamoa.txt"
    content = []

    # read content
    with open(path_to_file + file_name) as file_to_summarize:
        content = file_to_summarize.readlines()

    text_content = " ".join(content)
    summarized_text = summarizer.summarize(text_content)
    #print(summarized_text)
    file_name_summarized = file_name.split(".")[0] + "_summarized.txt"

    # write content to new file
    with open(path_to_file + file_name_summarized, 'w+') as file_to_summarize:
        file_to_summarize.writelines(summarized_text)

    print(file_name_summarized + " was created.")

if __name__ == "__main__":
    main()