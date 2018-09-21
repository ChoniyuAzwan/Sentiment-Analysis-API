from sklearn.feature_extraction.text import CountVectorizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np

app = Flask(__name__)
api = Api(app)

cv = pickle.load(open('CountVectorizer.sav', 'rb'))
dec_tree_classifier = pickle.load(open('dec_tree.sav', 'rb'))
ranforest_classifier = pickle.load(open('ranforest.sav', 'rb'))

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')

class PredictSentiment(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']
        
        # create stemmer
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        # vectorize the user's query and make a prediction
        y = stemmer.stem(user_query)

        # cv = CountVectorizer() #initially 15000+ returned.
        y = cv.transform(np.array([y])).toarray()

        y_pred_dec_tree = dec_tree_classifier.predict(y)
        y_pred_ranforest = ranforest_classifier.predict(y)

        # Output either 'Negative' or 'Positive' along with the score
        if y_pred_dec_tree == 0:
            dec_tree_result = 'Negative'
        else:
            dec_tree_result = 'Positive'

        if y_pred_ranforest == 0:
            ranforest_result = 'Negative'
        else:
            ranforest_result = 'Positive'

        # create JSON object
        output = {'decision tree': dec_tree_result, 'random forest': ranforest_result}

        return output


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictSentiment, '/')


if __name__ == '__main__':
    app.run(debug=True)
