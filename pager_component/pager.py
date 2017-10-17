```
total_row = models.Student.objects.all().count()  # 全部数据行数
page_info = PageInfo(request.GET.get("page"), total_row, 10, reverse("students"), 11)
students_list = models.Student.objects.all()[page_info.start():page_info.end()]
```

class PageInfo(object):
    def __init__(self, current_page, total_row, per_page, base_url, show_page=11):
        '''

        :param current_page: 当前页
        :param total_row: 总数据行数
        :param per_page: 每页显示几条数据
        :param base_url: url地址
        :param show_page: 显示几页
        '''
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        self.per_page = per_page
        # 求页码数
        x, y = divmod(total_row, per_page)
        if y:  # 如果余数不为0，页码+1
            x = x + 1
        self.total_page = x
        self.show_page = show_page
        self.base_url = base_url

    def start(self):
        return (self.current_page - 1) * self.per_page

    def end(self):
        return self.current_page * self.per_page

    def pager(self):
        page_list = []
        half_page = int((self.show_page - 1) / 2)  # 1／2显示几页

        # 总页数小于显示几页 <11
        if self.total_page < self.show_page:
            begin = 1
            stop = self.total_page + 1
        # 总页数大于显示几页 >11
        else:
            # 当前页小于一半
            if self.current_page <= half_page:
                begin = 1
                stop = self.show_page + 1
            # 当前页大于一半
            else:
                # 当前页+一半大于总页码
                if self.current_page + half_page > self.total_page:
                    begin = self.total_page - self.show_page + 1
                    stop = self.total_page + 1
                # 当前页+一半小于总页码
                else:
                    begin = self.current_page - half_page
                    stop = self.current_page + half_page + 1
        if self.current_page <= 1:
            prev = '<li><a href="#">上一页</a></li>'
        else:
            prev = '<li><a href="%s?page=%s">上一页</a></li>' % (self.base_url, self.current_page - 1,)
        page_list.append(prev)

        for i in range(begin, stop):
            if i == self.current_page:
                temp = '<li class="active"><a href="%s?page=%s">%s</a></li>' % (self.base_url, i, i)
            else:
                temp = '<li><a href="%s?page=%s">%s</a></li>' % (self.base_url, i, i)
            page_list.append(temp)

        if self.current_page >= self.total_page:
            nex = '<li><a href="#">下一页</a></li>'
        else:
            nex = '<li><a href="%s?page=%s">下一页</a></li>' % (self.base_url, self.current_page + 1,)
        page_list.append(nex)

        return ''.join(page_list)
