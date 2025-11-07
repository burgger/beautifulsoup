# Milestone-3
1. add new attributes in filter.SoupReplacer
2. modify ```__init.py```
3. modify ```element.py```
4. add 6 Test cases in ``test_ReplacerV2``
5. Re-write Task7 using SoupReplacerV2
```commandline
source venv/bin/activate
cd apps
python m3/Task7.py [INPUT PATH] [OUTPUT PATH]
```
## Technical Brief

In Milestone 3 we extend the Milestone2 API to make it a true “transformer 
interface” for BeautifulSoup’s parse pipeline.

| Aspect                     | Milestone 2 Implementation                       | Milestone 3 Enhancement                                                                                           |
| -------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------- |
| **Purpose**                | Simple tag rename (`og_tag → alt_tag`)           | General node transformation (name, attributes, side effects)                                                      |
| **Constructor**            | `SoupReplacer(og_tag, alt_tag)`                  | `SoupReplacer(name_xformer=None, attrs_xformer=None, xformer=None)`                                               |
| **Invocation Point**       | `Tag.__init__()` calls `maybe_replace(tag.name)` | `Tag.__init__()` calls `apply(tag)` → runs four steps sequentially: pair → name_xformer → attrs_xformer → xformer |
| **Transformation Scope**   | Tag name only                                    | Tag name + attributes + arbitrary mutation on the Tag object                                                      |
| **API Style**              | Positional pair mapping                          | Functional “transformer” pattern with lambdas or callables                                                        |

Using SoupReplacerV2 enables matching and modifying tags within a single line, while loading only the tag objects relevant to the 
current operation. This approach delivers solid performance even when handling large files.