# 🎹 音乐钢琴 - Android APP

一个可以在安卓手机上弹奏钢琴、学习曲谱的音乐 APP。

## ✨ 功能特性

- **钢琴弹奏** — 两个八度（C4-B5）完整键盘，支持触摸点击弹奏
- **8 首经典曲谱** — 小星星、欢乐颂、两只老虎、生日快乐、玛丽有只小羊羔、卡农（简化版）、云雀、铃儿响叮当
- **五线谱展示** — 实时显示当前演奏音符在五线谱上的位置，带歌词标注
- **自动演奏** — 点击播放即可自动演奏整首曲子
- **播放控制** — 暂停/停止/循环播放，速度可调（40-200 BPM）
- **进度跳转** — 点击进度条任意位置即可跳转到对应音符
- **新手引导** — 首次启动自动展示 6 步玩法教程，可随时重新查看
- **音色引擎** — 基于 Web Audio API 的泛音合成，模拟真实钢琴音色

## 📱 构建 APK 步骤

### 前提条件

- 安装 [Node.js](https://nodejs.org/) (v18+)
- 安装 [Android Studio](https://developer.android.com/studio)
- 配置 Android SDK（通过 Android Studio 的 SDK Manager）

### 步骤

1. **安装依赖**
   ```bash
   cd music-piano-android
   npm install
   ```

2. **同步 Capacitor 到 Android 项目**
   ```bash
   npx cap sync
   ```

3. **打开 Android Studio**
   ```bash
   npx cap open android
   ```
   或者手动用 Android Studio 打开 `android/` 文件夹。

4. **构建 APK**
   - 在 Android Studio 中，点击菜单 **Build → Build Bundle(s) / APK(s) → Build APK(s)**
   - 构建完成后，APK 文件位于：`android/app/build/outputs/apk/debug/app-debug.apk`

5. **安装到手机**
   - 用 USB 连接手机，开启开发者选项和 USB 调试
   - 点击 Android Studio 的 **Run** 按钮（▶），或手动传输 APK 到手机安装

### 构建 Release APK（可选）

1. 在 Android Studio 中，点击 **Build → Generate Signed Bundle / APK**
2. 创建或选择签名密钥
3. 选择 APK，完成构建

## 📂 项目结构

```
music-piano-android/
├── package.json              # Node.js 依赖配置
├── capacitor.config.ts       # Capacitor 配置
├── www/
│   └── index.html            # 主应用（单文件 HTML，含所有 CSS/JS）
├── android/                  # Android 原生项目
│   ├── app/
│   │   ├── build.gradle
│   │   ├── src/main/
│   │   │   ├── AndroidManifest.xml
│   │   │   ├── java/com/musicpiano/app/MainActivity.java
│   │   │   └── res/values/
│   │   └── proguard-rules.pro
│   ├── build.gradle
│   ├── settings.gradle
│   └── gradle.properties
└── README.md
```

## 🎮 玩法说明

### 自由弹奏
- 点击钢琴键盘的白键和黑键即可发声
- 触摸时琴键会亮起红色高亮

### 曲谱演奏
- 点击上方的歌曲卡片切换曲目
- 五线谱会自动加载该曲子的音符
- 点击播放按钮（▶）开始自动演奏
- 音符会在五线谱上实时高亮，并显示对应歌词

### 播放控制
- **▶ / ⏸** — 播放/暂停
- **⏹** — 停止并复位
- **🔁** — 开关循环播放
- **速度滑块** — 调节演奏速度（BPM）

### 进度跳转
- 点击进度条任意位置，即可跳转到曲子的对应位置

### 重新查看教程
- 点击右上角 **❓** 按钮，可随时重新打开玩法说明

## 🎵 内置曲目

| 曲目 | 难度 | 音符数 |
|------|------|--------|
| ⭐ 小星星 | 入门 | 56 |
| 🎶 欢乐颂 | 入门 | 64 |
| 🐯 两只老虎 | 入门 | 38 |
| 🎂 生日快乐 | 入门 | 32 |
| 🐑 玛丽有只小羊羔 | 入门 | 28 |
| 🎻 卡农（简化版） | 中等 | 40 |
| 🐦 云雀 | 中等 | 48 |
| 🔔 铃儿响叮当 | 入门 | 38 |

## 🛠 技术栈

- **前端**: 纯 HTML5 + CSS3 + Vanilla JS
- **音频**: Web Audio API（泛音合成）
- **移动端封装**: Capacitor 6
- **Android**: Gradle + AndroidX

## 📄 许可证

MIT License
