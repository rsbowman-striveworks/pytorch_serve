

"""
NoopService defines a no operational model handler.
"""
import logging
import time


class NoopService(object):
    """
    Noop Model handler implementation.

    Extend from BaseModelHandler is optional
    """

    def __init__(self):
        self._context = None
        self.initialized = False

    def initialize(self, context):
        """
        Initialize model. This will be called during model loading time

        :param context: model server context
        :return:
        """
        self.initialized = True
        self._context = context

    @staticmethod
    def preprocess(data):
        """
        Transform raw input into model input data.

        :param data: list of objects, raw input from request
        :return: list of model input data
        """
        return data

    @staticmethod
    def inference(model_input):
        """
        Internal inference methods

        :param model_input: transformed model input data
        :return: inference results
        """
        return model_input

    @staticmethod
    def postprocess(model_output):
        return ["OK"] * len(model_output)

    def handle(self, data, context):
        """
        Custom service entry point function.

        :param context: model server context
        :param data: list of objects, raw input from request
        :return: list of outputs to be send back to client
        """
        # Add your initialization code here
        request_processor = context.request_processor
        try:
            data = self.preprocess(data)
            data = self.inference(data)
            data = self.postprocess(data)

            context.set_response_content_type(0, "text/plain")

            return data
        except Exception as e:
            logging.error(e, exc_info=True)
            request_processor[0].report_status(500, "Unknown inference error.")
            return ["Error {}".format(str(e))] * len(data)


_service = NoopService()


def handle(data, context):
    if not _service.initialized:
        _service.initialize(context)

    if data is None:
        return None

    return _service.handle(data, context)
