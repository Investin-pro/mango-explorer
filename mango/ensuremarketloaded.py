# # ⚠ Warning
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
# NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# [🥭 Mango Markets](https://mango.markets/) support is available at:
#   [Docs](https://docs.mango.markets/)
#   [Discord](https://discord.gg/67jySBhxrg)
#   [Twitter](https://twitter.com/mangomarkets)
#   [Github](https://github.com/blockworks-foundation)
#   [Email](mailto:hello@blockworks.foundation)


from .context import Context
from .group import Group
from .market import Market
from .perpmarket import PerpMarketStub
from .serummarket import SerumMarketStub
from .spotmarket import SpotMarketStub

# # 🥭 ensure_market_loaded function
#
# This function ensures that a `Market` is 'loaded' and not a 'stub'. Stubs are handy for laoding in
# bulk, for instance in a market lookup, but real processing usually requires a fully loaded `Market`.
#
# This function simplifies turning a stub into a fully-loaded, usable market.


def ensure_market_loaded(context: Context, market: Market) -> Market:
    if isinstance(market, SerumMarketStub):
        return market.load(context)
    elif isinstance(market, SpotMarketStub):
        group: Group = Group.load(context, market.group_address)
        return market.load(context, group)
    elif isinstance(market, PerpMarketStub):
        group = Group.load(context, market.group_address)
        return market.load(context, group)

    return market
