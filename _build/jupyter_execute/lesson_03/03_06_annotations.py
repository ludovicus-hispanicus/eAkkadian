#!/usr/bin/env python
# coding: utf-8

# # Semantic Annotations
# 
# Semantic annotations refer to the process of adding metadata or labels to textual or multimedia content to provide additional contextual information and meaning. These annotations are used to enhance the understanding, organization, and retrieval of information by both humans and machines.
# 
# Semantic annotations can be applied at different levels, such as word or phrase level, document level, or even across multiple documents. The annotations may include various types of information, such as:
# 
#     1. Entity Recognition: Identifying and labeling named entities in text, such as names of people, organizations, locations, dates, etc. This helps in extracting specific information and understanding the relationships between entities.
# 
#     2. Part-of-Speech (POS) Tagging: Assigning grammatical tags to each word in a sentence, indicating its role and function (e.g., noun, verb, adjective, etc.). POS tagging aids in syntactic analysis and understanding the grammatical structure of text.
# 
#     3. Sentiment Analysis: Assigning sentiment labels (positive, negative, neutral) to text or parts of text to determine the overall sentiment expressed. This is useful in analyzing opinions, reviews, and social media sentiment.
# 
#     4. Topic Modeling: Assigning topics or themes to documents or text segments based on their content. Topic modeling algorithms can automatically discover the main subjects or themes discussed in a collection of documents.
# 
#     5. Relation Extraction: Identifying and labeling relationships between entities in text. For example, extracting relationships like "person A works for organization B" from a set of sentences.
# 
# Semantic annotations provide a way to make content more accessible, searchable, and interconnected. They enable advanced information retrieval techniques, such as faceted search, where users can filter and explore information based on different semantic criteria. Additionally, these annotations are essential for various natural language processing (NLP) tasks, such as information extraction, question answering, and text summarization.
# 
# The process of adding semantic annotations can be performed manually by human annotators or automated using machine learning techniques, such as named entity recognition (NER), sentiment analysis models, or topic modeling algorithms.
# 
# ## Annotating Akkadian Texts
# 
# First, we want to prepare the text:
# Let’s go for example to the website of ORACC. Let’s download, for example, SAA 5, 001 in ATF format. 
# 		
# 		[Copy and paste SAAo 05 001]
# 
# There are many ways to download it. We could download the whole SAA 05 or even SAA. 
# 
# We can’t go into details, but you can process the text using regex. If you want to process, for example, all the data of SAAo at once, you can follow the instruction in Compass, the Jupyter Notebook of Niek Veldlhuis.
# 
# Save the normalized text and the translation as two different text files.
# 
# 		[Show the files in the explorer]	
# 	
# For the annotations, we use INCEpTION. 
# 
# [Show INCEpTION website]
# 
# This is a powerful and flexible annotation platform that assists researchers and practitioners in efficiently annotating and preparing text data for training and evaluating NLP models. This annotation tool offers support for machine learning models integration, allowing users to train and improve NLP models using the annotated data.
# 
# Open the text file in INCEpTION and make the annotations you want. You can add many layers of annotations.
# 
# 		[Show the CONLLU file in Chrome]
# 
# In this way you can have a close reading of an Akkadian text and understand the syntactic relationship within a sentence. As stated before This data can be later used. An article on this topic by Matthew Ong and Shai Gordin is being reviewed.
# 
