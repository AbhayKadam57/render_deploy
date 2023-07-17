from mftool import Mftool
mf = Mftool()
import json
def getMutualfund_history_chart(code):
    q = mf.get_scheme_historical_nav(code,as_json=True)

    return json.loads(q)



