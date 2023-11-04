import requests
import json


class APICallMeaningCloud:
    _API_KEY = "7091f3f593aecf29aeaa6f8b7951bb22"
    _sample_api_result = {
        'status': {'code': '0', 'msg': 'OK', 'credits': '1', 'remaining_credits': '89'},
        'summary': 'A man in his 70s is dead after police say he was pinned between two vehicles '
                   'in the parking lot of a shopping plaza in Brampton on Friday afternoon. '
                   '“Unfortunately our victim happened to be walking between this parked car and '
                   'another parked car and when the Jeep struck that first parked car, it pinned '
                   'the victim,” Chin said. [...] The forensic identification unit is on scene '
                   'and the parking lot is expected to be closed for several hours.'}

    def getSummaryUrl(self, summary_url: str, num_sentences: int) -> str:
        """ Get the summary of any webpage.
            Inputs:
            - summary_url: the url of the desired webpage
            - num_sentences: the desired number of sentences in the summary

            Preconditions:
            - summary_url is a valid url
            - num_sentences >= 1
            """
        url = "https://api.meaningcloud.com/summarization-1.0"

        querystring = {"key": "7091f3f593aecf29aeaa6f8b7951bb22",
                       "url": summary_url,
                       "sentences": num_sentences}

        response = requests.post(url, params=querystring)

        json_file = response.json()
        return json_file["summary"]

    def getSummaryPlaintext(self, path: str, num_sentences: int) -> str:
        """ Get the summary of any plaintext file.
        Inputs:
        - path: the path of a plaintext file
        - num_sentences: the desired number of sentences in the summary

        Preconditions:
        - path is a valid path location
        - num_sentences >= 1
        """
        url = "https://api.meaningcloud.com/summarization-1.0"

        querystring = {"key": "7091f3f593aecf29aeaa6f8b7951bb22",
                       "url": path,
                       "sentences": num_sentences}

        response = requests.post(url, params=querystring)

        json_file = response.json()
        return json_file["summary"]

    # PRIVATE TEST CASES
    def _testJsonReturn(self) -> str:
        json_file = json.dumps(self._sample_api_result)
        json_dict = json.loads(json_file)
        return json_dict["summary"]
