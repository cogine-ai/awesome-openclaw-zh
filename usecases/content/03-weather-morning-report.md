# 天气晨报

> 每天 09:00 自动推送天气到 Telegram，包含早中晚夜四时段和异常天气提醒。

## 这个案例能帮你做什么

- 固定时间收到天气信息，不用每天手动打开天气 App。
- 自动输出体感温度、湿度、风速等关键字段。
- 极端天气自动提醒，通勤前更容易做出行决策。

## 你需要的 Skills（按类型）

| 类型 | Skill | 用途 | 来源 |
|---|---|---|---|
| 内置 | `weather` | 获取天气预报数据 | OpenClaw Built-in |
| 内置 | `telegram` | 推送晨报消息 | OpenClaw Built-in |
| 内置 | `cron` | 每日定时执行 | OpenClaw Built-in |

## 快速体验版（先跑一轮）

先执行一次即时预报：

```text
你是我的 OpenClaw 助手。
请帮我做“天气晨报”的预演版：
1. 按我配置的经纬度拉取今天天气。
2. 输出早晨/白天/傍晚/夜间四时段天气。
3. 包含体感温度、湿度、风速。
4. 本轮只生成消息文本，不发送到 Telegram。
```

## 稳定自动版（可长期运行）

### 1) 申请 API Key

```text
1. Visit https://yandex.ru/pogoda/b2b/smarthome
2. Register for free API key (50 requests/day)
3. Save key to environment: YANDEX_WEATHER_API_KEY
```

### 2) 位置配置

```javascript
const CONFIG = {
  lat: 51.53,      // Your latitude
  lon: 46.03,      // Your longitude
  lang: "ru_RU",   // Output language
  timezone: "Europe/Moscow"
};
```

### 3) 解析与格式化示例

```javascript
const conditionMap = {
  "clear": "ясно",
  "overcast": "пасмурно",
  "cloudy": "облачно",
  "rain": "дождь",
  "snow": "снег",
  "partly-cloudy": "переменная облачность"
};

function formatWeather(data) {
  const parts = data.forecasts[0].parts;
  return `
🌤️ Погода на сегодня:

🌅 Утро: ${parts.morning.temp_avg}°C (${conditionMap[parts.morning.condition]})
🌞 День: ${parts.day.temp_avg}°C (ощущается ${parts.day.feels_like}°C)
🌆 Вечер: ${parts.evening.temp_avg}°C
🌙 Ночь: ${parts.night.temp_avg}°C

💧 Влажность: ${parts.day.humidity}%
💨 Ветер: ${parts.day.wind_speed} м/с
  `.trim();
}
```

### 4) OpenClaw 执行提示词（自动版）

```text
你是我的 OpenClaw 助手，请执行“Weather Morning Report”。
请使用内置 Skills：weather、telegram、cron。

每天本地时间 09:00 执行：
1. 使用配置经纬度调用 Yandex Weather API。
2. 解析 morning/day/evening/night 四时段。
3. 将 condition code 转换为俄语描述。
4. 组装带 emoji 的天气消息。
5. 发送到 Telegram。
6. 把温度记录到 memory/weather-log.md。

告警条件：
- Temperature drops below -15°C
- Wind speed > 15 m/s
- Precipitation expected during commute hours
```

### 5) 调度配置

```json
{
  "schedule": "0 9 * * *",
  "timezone": "Europe/Moscow",
  "task": "weather_report",
  "action": "fetch_and_send_weather"
}
```

### 6) Telegram 消息模板

```markdown
🌤️ Погода на {{date}}

🌅 Утро: {{morning_temp}}°C ({{morning_condition}})
🌞 День: {{day_temp}}°C (ощущается {{feels_like}}°C)
🌆 Вечер: {{evening_temp}}°C
🌙 Ночь: {{night_temp}}°C

💧 Влажность: {{humidity}}%
💨 Ветер: {{wind_speed}} м/с

{{#alert}}
⚠️ {{alert_message}}
{{/alert}}
```

## 成功标准

- [ ] Delivered at 09:00 ± 2 minutes
- [ ] All 4 time periods included
- [ ] Alerts sent for extreme weather
- [ ] 30-day temperature trend available

## API 限额

| Tier | Requests/Day | Cost |
|---|---:|---|
| Free | 50 | $0 |
| Standard | 1000 | $10/month |
| Business | Unlimited | $50/month |

## 引用来源

- 来源仓库： [EvoLinkAI/awesome-openclaw-usecases-moltbook](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook)
- 原始条目： [usecases/03-weather-morning-report.md](https://github.com/EvoLinkAI/awesome-openclaw-usecases-moltbook/blob/main/usecases/03-weather-morning-report.md)
