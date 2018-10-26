# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import chat_pb2 as chat__pb2


class ChatServerStub(object):
  """The chat service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ReceiveMsg = channel.unary_unary(
        '/spartanchat.ChatServer/ReceiveMsg',
        request_serializer=chat__pb2.Message.SerializeToString,
        response_deserializer=chat__pb2.Message.FromString,
        )
    self.SendMsg = channel.unary_unary(
        '/spartanchat.ChatServer/SendMsg',
        request_serializer=chat__pb2.Message.SerializeToString,
        response_deserializer=chat__pb2.Message.FromString,
        )


class ChatServerServicer(object):
  """The chat service definition.
  """

  def ReceiveMsg(self, request, context):
    """This bi-directional stream makes it possible to send and receive Notes between 2 persons
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendMsg(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChatServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ReceiveMsg': grpc.unary_unary_rpc_method_handler(
          servicer.ReceiveMsg,
          request_deserializer=chat__pb2.Message.FromString,
          response_serializer=chat__pb2.Message.SerializeToString,
      ),
      'SendMsg': grpc.unary_unary_rpc_method_handler(
          servicer.SendMsg,
          request_deserializer=chat__pb2.Message.FromString,
          response_serializer=chat__pb2.Message.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'spartanchat.ChatServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class UserStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AddUser = channel.unary_unary(
        '/spartanchat.User/AddUser',
        request_serializer=chat__pb2.Message.SerializeToString,
        response_deserializer=chat__pb2.Message.FromString,
        )
    self.RemoveUser = channel.unary_unary(
        '/spartanchat.User/RemoveUser',
        request_serializer=chat__pb2.Message.SerializeToString,
        response_deserializer=chat__pb2.Message.FromString,
        )
    self.GetUsers = channel.unary_unary(
        '/spartanchat.User/GetUsers',
        request_serializer=chat__pb2.Message.SerializeToString,
        response_deserializer=chat__pb2.Message.FromString,
        )
    self.FriendRequest = channel.unary_unary(
        '/spartanchat.User/FriendRequest',
        request_serializer=chat__pb2.Message.SerializeToString,
        response_deserializer=chat__pb2.Message.FromString,
        )


class UserServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def AddUser(self, request, context):
    """This bi-directional stream makes it possible to send and receive Notes between 2 persons
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUsers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FriendRequest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AddUser': grpc.unary_unary_rpc_method_handler(
          servicer.AddUser,
          request_deserializer=chat__pb2.Message.FromString,
          response_serializer=chat__pb2.Message.SerializeToString,
      ),
      'RemoveUser': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveUser,
          request_deserializer=chat__pb2.Message.FromString,
          response_serializer=chat__pb2.Message.SerializeToString,
      ),
      'GetUsers': grpc.unary_unary_rpc_method_handler(
          servicer.GetUsers,
          request_deserializer=chat__pb2.Message.FromString,
          response_serializer=chat__pb2.Message.SerializeToString,
      ),
      'FriendRequest': grpc.unary_unary_rpc_method_handler(
          servicer.FriendRequest,
          request_deserializer=chat__pb2.Message.FromString,
          response_serializer=chat__pb2.Message.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'spartanchat.User', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
