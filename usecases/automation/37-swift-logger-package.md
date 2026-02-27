# Swift 日志包（TDD）

> 用 TDD 流程自动推进一个 Swift 日志包，从测试到发布形成闭环。

## 这个案例能帮你做什么

- 把“写包 + 写测试 + 发布”变成可重复执行流程。
- 先测后码，减少功能漂移和回归。
- 提前固化质量门槛，避免上线后再补测试。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `swift` | 编写与验证 Swift 包代码 | OpenClaw Built-in |
| 内置 | `git` | 版本管理与发布流程 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先用一个最小功能验证 TDD：

```text
你是我的 OpenClaw 助手。
请帮我做“Swift 日志包”的预演版：
1. 先定义最小 API 需求。
2. 先写 1 个失败测试（red）。
3. 再写最小实现让测试通过（green）。
4. 最后输出本轮重构建议（refactor）。
```

## 稳定自动版（可长期运行）

### 1) TDD 核心片段

```swift
// 1. Write test first
func testLoggerWritesToFile() {
  let logger = DelamainLogger(path: "/tmp/test.log")
  logger.info("test message")
  XCTAssertTrue(FileManager.default.fileExists("/tmp/test.log"))
}

// 2. Implement to pass test
public class DelamainLogger {
  public func info(_ message: String) {
    // Implementation
  }
}
```

### 2) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Swift Logger Package”。
请使用内置 Skills：swift、git。

开发流程：
1. 定义 API 需求。
2. 编写单元测试（red）。
3. 以最小实现通过测试（green）。
4. 在测试通过前提下重构。
5. 完成 API 文档。
6. 打版本标签。
7. 发布到 GitHub。

质量门槛：
- 100% test coverage
- SwiftLint passing
- Documentation complete
```

## 成功标准

- [ ] All tests passing
- [ ] Published to GitHub
- [ ] Documentation complete

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/37-swift-logger-package.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/37-swift-logger-package.md)
