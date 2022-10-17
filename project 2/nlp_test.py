import nlp
import pytest
from npl import *
from unittest.mock import MagicMock

def test_nlp_access():
    client = language_v1.LanguageServiceClient()
    assert client


def test_input_file():
    filelist = os.listdir("result")
    if len(filelist) == 0:
        print("Valid input text file")
    else:
        print("INVALID text input file")


def test_sentiment_analyze():
    client = language_v1.LanguageServiceClient()

    content = "Today, Boston is a thriving center of scientific research. The Boston area's many colleges and universities make it a world leader in higher education,[20] including law, medicine, engineering and business, and the city is considered to be a global pioneer in innovation and entrepreneurship, with nearly 5,000 startups.[21][22][23] Boston's economic base also includes finance,[24] professional and business services, biotechnology, information technology and government activities.[25] Households in the city claim the highest average rate of philanthropy in the United States;[26] businesses and institutions rank among the top in the country for environmental sustainability and investment.[27] The city has one of the highest costs of living in the United States[28][29] as it has undergone gentrification,[30] though it remains high on world livability rankings.[31]"
    document = language_v1.Document(
        content=content, type_=language_v1.Document.Type.PLAIN_TEXT
    )
    annotations = client.analyze_sentiment(document=document)
    assert annotations is not None
    assert annotations.document_sentiment.score is not None