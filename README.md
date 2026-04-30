# 📧 Spam Email Detection System

A machine learning web application that detects spam messages using 
Natural Language Processing (NLP) and Naive Bayes classification.

## 🌐 Live Demo
[https://spam-detection-anees.streamlit.app](https://spam-detection-anees.streamlit.app)

## 📌 Features
- Detects spam messages with 97.6% accuracy
- Real time prediction via web interface
- Built with NLP preprocessing pipeline
- Trained on 5572 real SMS messages

## 🛠️ Tech Stack
| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Scikit-learn | Machine learning models |
| NLTK | Text preprocessing |
| TF-IDF | Text to numbers conversion |
| Streamlit | Web application |
| Pickle | Model saving |

## 📊 Model Results
| Metric | Score |
|---|---|
| Accuracy | 97.6% |
| Precision | 100% |
| Recall | 82% |
| F1 Score | 90.1% |

## 🚀 How to Run Locally
1. Clone the repository
   git clone https://github.com/Anees2633/spam-detection.git

2. Install libraries
   pip install -r requirements.txt

3. Run the app
   streamlit run app.py

## 📁 Project Structure
spam-detection/
├── app.py                  
├── spam_model.pkl          
├── tfidf_vectorizer.pkl    
└── requirements.txt        

## 👤 Author
Muhammad Anees
CS Graduate