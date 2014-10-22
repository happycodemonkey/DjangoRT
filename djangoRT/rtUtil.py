import rt
from djangoRT_settings import RT_HOST, RT_UN, RT_PW

class DjangoRt:
	
	def __init__(self):
		self.rtHost = RT_HOST
		self.rtUn = RT_UN
		self.rtPw = RT_PW

		self.tracker = rt.Rt(self.rtHost, self.rtUn, self.rtPw, basic_auth=(self.rtUn, self.rtPw))
		self.tracker.login()

	def getUserTickets(self, userEmail):
		return self.tracker.search(Queue=rt.ALL_QUEUES, raw_query="Requestors='" + userEmail + "'")

	def getTicket(self, ticketId):
		return self.tracker.get_ticket(ticketId)

	def getTicketHistory(self, ticketId):
		return self.tracker.get_history(ticketId)

	def createTicket(self, ticket):
		return None

