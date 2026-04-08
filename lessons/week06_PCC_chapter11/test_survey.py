from l02_testing_classes import AnonymousSurvey

def test_store_single_response ():
    """Test that a single response is stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_responses('English')
    assert 'English' in language_survey.responses

def test_store_three_responses():
    """Test that three individual responses are stored properly."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_responses(response)
    for response in responses:
        assert response in language_survey.responses