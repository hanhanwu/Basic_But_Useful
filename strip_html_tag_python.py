class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)



def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
    
    
s = """<p class="articleParagraph enarticleParagraph">The United States – which had previously relied on its massive cultural industry to do its tourism promotion for it – is seriously targeting travellers for the first time. In light of the competition, the <span class="companylink">Canadian government</span> could do more for the Canadian industry and to build Canada's brand in the world.</p><p class="articleParagraph enarticleParagraph">The U.S. has shattered records for international visitors in four of the past five years. It is now seeking to push that growth further still with Brand USA, a public-private partnership established by an Act of Congress in 2010 to “spearhead the nation's first global marketing effort to promote the United States as a premier travel destination.” Canada is one of the countries being targeted by the $200-million campaign.</p>"""
print strip_tags(s)
