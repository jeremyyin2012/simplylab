import unittest

from loguru import logger

from simplylab.providers.openrouter import middle_out


class MyTestCase(unittest.TestCase):
    def test_middle_out(self):
        content = """
Text generation and embeddings models process text in chunks called tokens. Tokens represent commonly occurring sequences of characters. For example, the string " tokenization" is decomposed as " token" and "ization", while a short and common word like " the" is represented as a single token. Note that in a sentence, the first token of each word typically starts with a space character. Check out our tokenizer tool to test specific strings and see how they are translated into tokens. As a rough rule of thumb, 1 token is approximately 4 characters or 0.75 words for English text.

One limitation to keep in mind is that for a text generation model the prompt and the generated output combined must be no more than the model's maximum context length. For embeddings models (which do not output tokens), the input must be shorter than the model's maximum context length. The maximum context lengths for each text generation and embeddings model can be found in the model index.
        """
        model_name = "gpt-3.5-turbo"
        limit = 100
        chat_content = middle_out(content, model_name, limit)
        logger.debug(chat_content)

        import tiktoken
        encoding = tiktoken.encoding_for_model(model_name)
        tokens = encoding.encode(chat_content)
        token_count = len(tokens)
        logger.debug(f"{token_count=}, {limit=}")
        res = token_count <= limit
        self.assertEqual(res, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
