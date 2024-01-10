import streamlit as st
from docx import Document
import os

def find_text_in_docx_folder(folder_path, special_field):
    # 存储找到的文本
    found_texts = []

    # 获取文件夹中的所有 Word 文档
    for filename in os.listdir(folder_path):
        if filename.endswith(".docx"):
            doc_path = os.path.join(folder_path, filename)

            # 打开 Word 文档
            doc = Document(doc_path)

            # 遍历文档中的段落
            for paragraph in doc.paragraphs:
                # 检查段落是否包含特定字段
                if special_field in paragraph.text:
                    # 如果包含特定字段，将文本添加到列表中
                    found_texts.append(paragraph.text)

    return found_texts

# Streamlit App
def main():
    st.title("文本检索应用")

    # 输入文件路径
    file_path = st.text_input("请输入文件路径：")

    # 输入关键词
    keyword = st.text_input("请输入关键词：")

    # 检索按钮
    if st.button("开始检索"):
        if os.path.exists(file_path) and file_path.endswith(".docx"):
            # 进行文本检索
            found_texts = find_text_in_docx_folder(file_path, keyword)

            # 显示检索结果
            st.subheader("检索结果：")
            if found_texts:
                for text in found_texts:
                    st.write(text)
            else:
                st.write("未找到包含关键词的文本。")
        else:
            st.warning("请提供有效的 .docx 文件路径。")

if __name__ == "__main__":
    main()
