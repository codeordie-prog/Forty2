
from langchain_community.tools.pubmed.tool import PubmedQueryRun

tool = PubmedQueryRun()

response = tool.invoke("what causes nose bleeds")

print(response)