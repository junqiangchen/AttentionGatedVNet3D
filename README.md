# Attention Gated VNet3D Model for KiTS19——2019 Kidney Tumor Segmentation Challenge
> This is an example of combining VNet3D and AttentionGating.(re)implemented the model with tensorflow in the paper of "Ozan Oktay, Jo Schlemper, Loic Le Folgoc, Matthew Lee, Mattias Heinrich, Kazunari Misawa, Kensaku Mori, Steven McDonagh, Nils Y Hammerla, Bernhard Kainz, Ben Glocker, Daniel Rueckert.(2018) Attention U-Net: Learning Where to Look for the Pancreas"
![](KiTS19_header.png)

## Prerequisities
The following dependencies are needed:
- numpy >= 1.11.1
- opencv-python >=3.3.0
- tensorflow-gpu ==1.8.0
- pandas >=0.20.1
- scikit-learn >= 0.17.1

## How to Use

*Preprocess*
follow KiTS19——2019 Kidney Tumor Segmentation Challenge project

* the AGVNet3D model

![](AGUnet.PNG)

* the Attention Gated model

![](AGModel.PNG)

## Prerequisities
Attention U-Net model can find from here:https://github.com/ozan-oktay/Attention-Gated-Networks

## Result
**1、Kidney Segmentation**
* the train loss

![](kidneyloss.png)

* 200-209case dice value and result

![](dicevalue.PNG)

* segmentation result can find in the video of attengat.avi

## Contact
* https://github.com/junqiangchen
* email: 1207173174@qq.com
* Contact: junqiangChen
* WeChat Number: 1207173174
* WeChat Public number: 最新医学影像技术
