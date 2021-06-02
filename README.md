## 这是如何在您的烧瓶应用程序中使用 loguru 的简单示例
只需创建一个新的 InterceptHandler 并将其添加到您的应用程序中即可。应该在您的配置文件中配置不同的设置，以便于更改设置。

日志记录就像这样简单：

```python
from loguru import logger

logger.info("I am logging from loguru!")
```

