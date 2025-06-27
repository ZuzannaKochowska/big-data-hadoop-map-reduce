from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import pos_tag
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')




lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words('english')

print(lemmatizer.lemmatize('computers'))
print(pos_tag(['big']))
print(pos_tag(['commonly']))