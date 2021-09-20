from rest_framework import pagination

class AccountPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 50
    
    def get_pagination_response(self, data):
        response = Response(data)
        request['count'] = self.page.pagination.count
        request['next'] = self.get_next_link()
        request['previous'] = self.get_previous_link()
        return response
