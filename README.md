# Earthquake-early-warning-system
一、簡介

近幾年，在各地所發生的強烈地震時有所聞，許多科學家認為地球進入了地震的活躍期，而台灣位於歐亞大陸板塊與菲律賓海板塊交界，地震頻繁。地震所造成的死亡人數，往往和人們無法提前預警逃生有很大的關係，例如九二一大地震造成了2,415人死亡，29人失蹤，11,305人受傷，如果我們能提前得知地震的發生，並快速逃生，那就能大大降低傷害，減少死亡人數。
    因此我們想設計地震預警警報器，當地震來臨時，可以提前預警，發出警告聲和閃爍警示燈，提醒人們地震來臨，請快速逃離至空曠區或躲避至桌下。
    
二、實作所需材料

材料名稱	數量	來源
杜邦線(公母)	3條	周霈菱
麵包板	1個	
LED燈	1個	張秝榕
蜂鳴器	1個	
電阻	1個	
電線	1捆	

三、使用的現有軟體與來源

1.【Python3】https://www.python.org/download/releases/3.0/

2.【Django】https://www.djangoproject.com/

3.【python-RPi.GPIO】https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/

四、系統流程圖

 
圖一 系統流程圖

上圖為系統流程圖(如圖一)，當我們收到地震資訊時，會進入Django進行連線處理，之後呼叫warning.py 檔，執行地震警示(LED燈閃爍、蜂鳴器叫)，最後在網頁顯示資訊。

五、實作過程

    實作的過程主要分成「電路實作」和「程式撰寫」兩部分。
    在電路實作的部分，先參照Raspberry Pi 3的接腳圖(如圖二)，在麵包板上接上LED、電阻和蜂鳴器，並供電和接地，(如圖三)。
    在程式撰寫的部分，用Python撰寫所有程式。先分別寫LED和蜂鳴器的程式碼，再來用Django架設伺服器進行連線處理，最後將所有功能集合在一起，當接收到地震資訊時，LED和蜂鳴器會發出警示提醒大家快速逃生。
    在實作過程遇到的困難為不知道如何傳資訊給Raspberry Pi 3，解決方法為用Django進行傳輸。
 
圖二 Raspberry Pi 3的接腳圖
 
圖三 電路圖

六、網頁操作說明

因為地震的預警系統無法進行地震分級，需要等到中央氣象局統計完整個地震資料後，才能獲得地震級數，所以我們又多做了這個網頁(如圖四)。首先，我們先看地圖中紅色的球，此點代表震央，球距離地圖的高度代表地震的深度，球上的數字則代表規模，柱狀圖依照下方震度對照表代表各地震度大小(如圖五)，我們可以用滑鼠對地圖進行拖移、放大、縮小，如果想要看更多地層資訊，可以勾選上方的斷層、地形、土壤液化等相關選項(如圖六)，最後我們可以點右上方的月曆，選擇不同日期觀看不同時間地震的資訊。
 
圖四 網頁
 
圖五 地震資訊(震央、震度)
 
圖六 地震資訊(斷層、地形、土壤液化)

七、工作分配構想：李恩賢、張秝榕、陳昊、周霈菱

	材料準備：張秝榕、周霈菱
	程式撰寫：李恩賢、陳昊
	文件撰寫、PPT製作：張秝榕、周霈菱
	電路圖實作與繪製：張秝榕、周霈菱
	影片製作：李恩賢、張秝榕、陳昊、周霈菱

八、影片連結：https://www.youtube.com/watch?v=HkXT5slSXOw&feature=youtu.be

九、參考來源

1.【接腳圖】http://magicjackting.pixnet.net/blog/post/128014810
2.【硬pi製作】https://sites.google.com/site/raspberrypidiy/basic/gpioled
3.【Driving a buzzer in python】https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=13955
4.【Writing tour first Django app】https://docs.djangoproject.com/en/2.0/intro/tutorial01/
