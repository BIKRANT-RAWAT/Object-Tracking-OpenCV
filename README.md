# 🎯 Object Tracking using OpenCV

This repository showcases **multiple classical object tracking algorithms available in OpenCV**, applied on a sample video (`Eagle.mp4`) or live with webcam. Each tracker is implemented separately so we can **experiment, compare, and understand their behavior** in real-world video scenarios.

The project also demonstrates **video writing**, where tracking results are saved as an output video (`tracking_output.mp4`).

---

## 📽️ Demo (Input vs Output)

Below is a **side-by-side comparison** of the original input video and the tracked output video using boosting based tracker.

<table> <tr> <th>Input Video</th> <th>Tracking Output</th> </tr> <tr> <td align="center"> <a href="Eagle.mp4"> ▶️ Click to play Eagle.mp4 </a> </td> <td align="center"> <a href="tracking_output.mp4"> ▶️ Click to play tracking_output.mp4 </a> </td> </tr> </table>

---

## 📂 Repository Structure

```
├── Eagle.mp4               # Input video for tracking
├── tracking_output.mp4     # Output video with tracking results
├── boosting.py             # BOOSTING tracker implementation
├── csrt.py                 # CSRT tracker (high accuracy)
├── goturn.py               # GOTURN deep learning based tracker
├── kcf.py                  # KCF tracker (fast & efficient)
├── medianflow.py           # MedianFlow tracker
├── mil.py                  # MIL tracker
├── mosse.py                # MOSSE tracker (very fast)
├── tld.py                  # TLD tracker
├── video_writer.py         # Utility for saving output video
├── stream_yolo11.py        # Ultralytics yolo11 
├── requirements.txt        # Project dependencies
```

---

## 🧠 Trackers Covered

This project includes implementations of the following OpenCV trackers:

* **BOOSTING** – Online boosting-based tracker
* **MIL** – Multiple Instance Learning tracker
* **KCF** – Kernelized Correlation Filters
* **CSRT** – Discriminative Correlation Filter with Channel and Spatial Reliability
* **MOSSE** – Extremely fast correlation-based tracker
* **MedianFlow** – Robust for predictable motion
* **TLD** – Tracking, Learning, and Detection
* **GOTURN** – Deep learning based object tracker
* **YOLO11** – Ultralytics yolo11 based object tracker

Each tracker has different **speed vs accuracy trade-offs**, making this repo ideal for learning and benchmarking.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/BIKRANT-RAWAT/Object-Tracking-OpenCV.git
cd Object-Tracking-OpenCV
```

Install dependencies:

```bash
pip install -r requirements.txt
```

> ⚠️ Note: Some trackers require **opencv-contrib-python**.

> ⚠️ Note: Make sure to download goturn caffe model to run goturn.

---

## ▶️ How to Run

Run any tracker script directly, for example:

```bash
python csrt.py
```

Or switch trackers by running the respective file:

```bash
python kcf.py
python mosse.py
python goturn.py
```

The output video will be saved automatically.

---

## 📌 Key Learnings

* Practical understanding of **classical object tracking algorithms**
* How OpenCV trackers differ in **performance and robustness**
* Frame-by-frame video processing
* Writing inference results back to a video file

---

## 🚀 Future Improvements

* Unified tracker selection via CLI arguments
* FPS benchmarking across trackers
* Multi-object tracking support
* Deep learning–based trackers comparison

---
🙏 Acknowledgement

This project was build under the guidance of pwskills team and was inspired by the OpenCV community and official documentation, which provide robust implementations of classical object tracking algorithms.

Special thanks to:

OpenCV Contributors for maintaining and improving tracking APIs

Open-source educators and researchers whose examples and discussions helped in understanding tracker behavior

The broader computer vision open-source ecosystem for making experimentation and learning accessible

---

## 👤 Author

**Bikrant Rawat**
Data Scientist | Computer Vision | Deep Learning

📫 Reach out: **[connect.bikrantrawat@gmail.com](mailto:connect.bikrantrawat@gmail.com)**

---

⭐ If you find this useful, consider starring the repository!
