# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import label_classifier_pb2 as label__classifier__pb2


class LabelTypeStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Run_classifier = channel.stream_stream(
        '/label_class.LabelType/Run_classifier',
        request_serializer=label__classifier__pb2.Label.SerializeToString,
        response_deserializer=label__classifier__pb2.Label_class.FromString,
        )


class LabelTypeServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Run_classifier(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LabelTypeServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Run_classifier': grpc.stream_stream_rpc_method_handler(
          servicer.Run_classifier,
          request_deserializer=label__classifier__pb2.Label.FromString,
          response_serializer=label__classifier__pb2.Label_class.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'label_class.LabelType', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
