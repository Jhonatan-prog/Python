## Getting Info and storing them
import re
import time
import asyncio
import numpy as np
from requests_html import HTML, AsyncHTMLSession

if __name__ == "__main__":
    session = AsyncHTMLSession()
    regex = re.compile(f'')

    async def wikiFandom():
        start_time = time.perf_counter()

        request = await session.get('https://genshin-impact.fandom.com/es/wiki/Eula')
        ## Links
        divsL = request.html.find('div')
        global linksContainer
        linksContainer = [webLink.links for webLink in divsL if webLink.links != set()]
        
        await asyncio.sleep(1)

        elapsed = time.perf_counter() - start_time
        print(f"The function One was executed in {elapsed:0.2f} seconds.")
        print()

    async def dlPrivateS():
        start_time = time.perf_counter()

        request = await session.get('https://dlprivateserver.com/guia-de-genshin-impact-eula-habilidades-fecha-de-lanzamiento-como-obtenerla-y-mas/')
        ## Links
        divsL = request.html.find('div')
        for webLink in divsL:
            if webLink.links != set():
                linksContainer.append(webLink.links)
        print()

        elapsed = time.perf_counter() - start_time
        print(f"The function Two executed in {elapsed:0.2f} seconds.")

    ## creating the event loop
    session.run(wikiFandom,dlPrivateS)

    ## pushing data to Series
    import pandas as pd
    import numpy as np 

    linkSeries = pd.Series(linksContainer)
    linkSeries.index = np.arange(1, len(linkSeries) + 1)
    print(linkSeries)
    
else:
    print("You are in other module")