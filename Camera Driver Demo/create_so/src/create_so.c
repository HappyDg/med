#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "nncam.h"


HNnCam g_hcam = NULL;
void* g_pImageData = NULL;
unsigned g_total = 0;
unsigned g_totalstill = 0;

const int bytesPerPixel = 3; /// red, green, blue
const int fileHeaderSize = 14;
const int infoHeaderSize = 40;

void generateBitmapImage(unsigned char *image, int height, int width, char* imageFileName);
unsigned char* createBitmapFileHeader(int height, int width, int paddingSize);
unsigned char* createBitmapInfoHeader(int height, int width);
void main_sample(unsigned char * p, int length);

//int test(void);
//extern "C"{
//int add(int x,int y);
//}





static void __stdcall EventCallback(unsigned nEvent, void* pCallbackCtx)
{
    if (NNCAM_EVENT_IMAGE == nEvent)
    {
        NncamFrameInfoV2 info = { 0 };
        HRESULT hr = Nncam_PullImageV2(g_hcam, g_pImageData, 24, &info);
        if (FAILED(hr))
        {
            //printf("failed to pull image, hr = %08x\n", hr);
        }
        else
        {
            /* After we get the image data, we can do anything for the data we want to do */
            printf("pull image ok, total = %u, resolution = %u x %u\n", ++g_total, info.width, info.height);
            main_sample((unsigned char *)g_pImageData,(info.width)*(info.height)*3);
        }
        Nncam_Stop(g_hcam);
        Nncam_Close(g_hcam);
        exit(0);

    }
    else if (NNCAM_EVENT_STILLIMAGE == nEvent)
    {
        NncamFrameInfoV2 info = { 0 };

        HRESULT hr = Nncam_PullStillImageV2(g_hcam, g_pImageData, 24, &info);
        if (FAILED(hr))
        {
            //printf("failed to pull still image, hr = %08x\n", hr);
        }
        else
        {
            /* After we get the image data, we can do anything for the data we want to do */
            printf("pull still image ok, total = %u, resolution = %u x %u\n", ++g_totalstill, info.width, info.height);
            main_sample((unsigned char *)g_pImageData,(info.width)*(info.height)*3);
        }
    }
    else
    {
        //printf("event callback: %d\n", nEvent);
    }

}

int test_add(int x,int y)
{
   return x+y;
}

int test(void)
{
	/*枚举相机支持功能和部分参数code*/
/*
    NncamInstV2 arr[NNCAM_MAX];
	unsigned cnt = Nncam_EnumV2(arr);
	printf("cnt=%d\r\n",cnt);
    printf("device name=%s,id=%s\r\n",arr[0].displayname,arr[0].id);
    printf("NNCAM_FLAG_USB30=0x%08x\r\n",arr[0].model->flag&NNCAM_FLAG_USB30);//这里有很多flag，读取可能有用的就好
    printf("NNCAM_FLAG_CMOS=0x%08x\r\n",arr[0].model->flag&NNCAM_FLAG_CMOS);
    printf("NNCAM_FLAG_CCD_PROGRESSIVE=0x%08x\r\n",arr[0].model->flag&NNCAM_FLAG_CCD_PROGRESSIVE);
    printf("NNCAM_FLAG_CCD_INTERLACED=0x%08x\r\n",arr[0].model->flag&NNCAM_FLAG_CCD_INTERLACED);
    printf("NNCAM_FLAG_TRIGGER_SOFTWARE=0x%08x\r\n",arr[0].model->flag&NNCAM_FLAG_TRIGGER_SOFTWARE);
    printf("NNCAM_FLAG_TRIGGER_EXTERNAL=0x%08x\r\n",arr[0].model->flag&NNCAM_FLAG_TRIGGER_EXTERNAL);
    printf("NNCAM_FLAG_TRIGGER_SINGLE=0x%08x\r\n",arr[0].model->flag&NNCAM_FLAG_TRIGGER_SINGLE);
    printf("NNCAM_FLAG_BLACKLEVEL=0x%08x\r\n",arr[0].model->flag&NNCAM_FLAG_BLACKLEVEL);
    printf("NNCAM_FLAG_AUTO_FOCUS=0x%08x\r\n",arr[0].model->flag&NNCAM_FLAG_AUTO_FOCUS);
    printf("NNCAM_FLAG_BUFFER=0x%08x\r\n",arr[0].model->flag&NNCAM_FLAG_BUFFER);
    printf("NNCAM_FLAG_RGB888=0x%08x\r\n",arr[0].model->flag&NNCAM_FLAG_RGB888);
    printf("NNCAM_FLAG_RAW8=0x%08x\r\n",arr[0].model->flag&NNCAM_FLAG_RAW8);
    printf("number of speed level=%d\r\n",arr[0].model->maxspeed);
    printf("number of preview resolution=%d\r\n",arr[0].model->preview);
    printf("number of still resolution=%d\r\n",arr[0].model->still);
    printf("res width=%d,res height=%d\r\n",arr[0].model->res[0].width,arr[0].model->res[0].height);
    g_hcam = Nncam_Open(NULL);
    char *SerialNumber = (char *)malloc(32);
    char *FwVersion = (char *)malloc(16);
    char *HwVersion = (char *)malloc(16);
    char *ProductionDate = (char *)malloc(10);
    Nncam_get_SerialNumber(g_hcam,SerialNumber);
    Nncam_get_FwVersion(g_hcam,FwVersion);
    Nncam_get_HwVersion(g_hcam,HwVersion);
    Nncam_get_ProductionDate(g_hcam,ProductionDate);
    printf("SerialNumber=%s\nFwVersion=%s\nHwVersion=%s\nProductionDate=%s\r\n",SerialNumber,FwVersion,HwVersion,ProductionDate);
    return 0;
*/

    g_hcam = Nncam_Open(NULL);
    if (NULL == g_hcam)
    {
        printf("no camera found\n");
        return -1;
    }
    // 896*684    1792*1374    3584*2748
    int nWidth = 0, nHeight = 0,auto_expo_flag=0xFF;
    unsigned Time=0;
    int i = 0;
    HRESULT hr = Nncam_get_Size(g_hcam, &nWidth, &nHeight);
    //printf("before size:Width=%d,Height=%d\r\n",nWidth,nHeight);
    Nncam_put_Size(g_hcam,1792,1374);
    HRESULT hr1 = Nncam_get_Size(g_hcam, &nWidth, &nHeight);
    //printf("after size:Width=%d,Height=%d\r\n",nWidth,nHeight);

//    Nncam_get_AutoExpoEnable(g_hcam,&auto_expo_flag);
//    printf("before:auto_expo_flag=%d\r\n",auto_expo_flag);
//    Nncam_put_AutoExpoEnable(g_hcam,0);
//    Nncam_get_AutoExpoEnable(g_hcam,&auto_expo_flag);
//    printf("after:auto_expo_flag=%d\r\n",auto_expo_flag);


//    Nncam_get_ExpoTime(g_hcam,&Time);
//    printf("before:time=%d\r\n",Time);
//    Nncam_put_ExpoTime(g_hcam,200);
//    Nncam_get_ExpoTime(g_hcam,&Time);
//    printf("after:time=%d\r\n",Time);

    if (FAILED(hr))
        printf("failed to get size, hr = %08x\n", hr);
    else
    {
        g_pImageData = malloc(TDIBWIDTHBYTES(24 * nWidth) * nHeight);
        if (NULL == g_pImageData){
        	//printf("failed to malloc\n");
        }

        else
        {
        	//this is push mode
        	//hr = Nncam_StartPushModeV2(g_hcam, datacallbackv2, NULL);
        	//this is pull mode

            hr = Nncam_StartPullModeWithCallback(g_hcam, EventCallback, NULL);
            if (FAILED(hr)){
            	printf("failed to start camera, hr = %08x\n", hr);
            }
            else
            {
                printf("press any key to exit\n");
                getc(stdin);
            }
        }
    }


    /* cleanup */
    printf("clean up\r\n");

    Nncam_Close(g_hcam);
    if (g_pImageData)
        free(g_pImageData);
    return 0;
}



int i =0;
void main_sample(unsigned char * p, int length){
	//printf("start to create\r\n");
// 896*684    1792*1374    3584*2748
    int height = 1374;
    int width = 1792;
    char b[500];
    //printf("point test A\r\n");
    unsigned char image[height][width][bytesPerPixel];
    //printf("image=%d\r\n",image);
    //printf("point test B\r\n");
    sprintf(b,"%d",i);
    char* imageFileName = "bitmapImage.bmp";
    imageFileName = strcat(b,imageFileName);
    i++;
    //printf("point test C\r\n");
//    int i, j;
//    for(i=0; i<height; i++){
//        for(j=0; j<width; j++){
//            image[i][j][2] = (unsigned char)((double)i/height*255); ///red
//            image[i][j][1] = (unsigned char)((double)j/width*255); ///green
//            image[i][j][0] = (unsigned char)(((double)i+j)/(height+width)*255); ///blue
//        }
//    }

    //printf("point test D\r\n");

    if (length <= height*width*bytesPerPixel){
    	memcpy(image,p,length);
    }
    else{
    	return;
    }
    //printf("point test E\r\n");
    generateBitmapImage((unsigned char *)image, height, width, imageFileName);
    //printf("point test F\r\n");
    printf("Image generated!!\r\n");
}


void generateBitmapImage(unsigned char *image, int height, int width, char* imageFileName){

    unsigned char padding[3] = {0, 0, 0};
    int paddingSize = (4 - (width*bytesPerPixel) % 4) % 4;

    unsigned char* fileHeader = createBitmapFileHeader(height, width, paddingSize);
    unsigned char* infoHeader = createBitmapInfoHeader(height, width);

    if ((fileHeader == NULL)||(infoHeader == NULL)){
      return;
    }

    FILE* imageFile = fopen(imageFileName, "wb");

    fwrite(fileHeader, 1, fileHeaderSize, imageFile);
    fwrite(infoHeader, 1, infoHeaderSize, imageFile);

    int i;
    for(i=0; i<height; i++){
        fwrite(image+(i*width*bytesPerPixel), bytesPerPixel, width, imageFile);
        fwrite(padding, 1, paddingSize, imageFile);
    }

    fclose(imageFile);
    free(fileHeader);
    free(infoHeader);
}

unsigned char* createBitmapFileHeader(int height, int width, int paddingSize){
    int fileSize = fileHeaderSize + infoHeaderSize + (bytesPerPixel*width+paddingSize) * height;

//    static unsigned char fileHeader[] = {
//        0,0, /// signature
//        0,0,0,0, /// image file size in bytes
//        0,0,0,0, /// reserved
//        0,0,0,0, /// start of pixel array
//    };
    unsigned char *fileHeader = (unsigned char *)malloc(14);

    if (fileHeader == NULL){
       return NULL;
    }
    else{
       memset(fileHeader,0,14);
    }


    fileHeader[ 0] = (unsigned char)('B');
    fileHeader[ 1] = (unsigned char)('M');
    fileHeader[ 2] = (unsigned char)(fileSize    );
    fileHeader[ 3] = (unsigned char)(fileSize>> 8);
    fileHeader[ 4] = (unsigned char)(fileSize>>16);
    fileHeader[ 5] = (unsigned char)(fileSize>>24);
    fileHeader[10] = (unsigned char)(fileHeaderSize + infoHeaderSize);

    return fileHeader;
}

unsigned char* createBitmapInfoHeader(int height, int width){
//    static unsigned char infoHeader[] = {
//        0,0,0,0, /// header size
//        0,0,0,0, /// image width
//        0,0,0,0, /// image height
//        0,0, /// number of color planes
//        0,0, /// bits per pixel
//        0,0,0,0, /// compression
//        0,0,0,0, /// image size
//        0,0,0,0, /// horizontal resolution
//        0,0,0,0, /// vertical resolution
//        0,0,0,0, /// colors in color table
//        0,0,0,0, /// important color count
//    };
    unsigned char *infoHeader = (unsigned char *)malloc(40);

    if (infoHeader == NULL){
       return NULL;
    }
    else{
       memset(infoHeader,0,40);
    }

    infoHeader[ 0] = (unsigned char)(infoHeaderSize);
    infoHeader[ 4] = (unsigned char)(width    );
    infoHeader[ 5] = (unsigned char)(width>> 8);
    infoHeader[ 6] = (unsigned char)(width>>16);
    infoHeader[ 7] = (unsigned char)(width>>24);
    infoHeader[ 8] = (unsigned char)(height    );
    infoHeader[ 9] = (unsigned char)(height>> 8);
    infoHeader[10] = (unsigned char)(height>>16);
    infoHeader[11] = (unsigned char)(height>>24);
    infoHeader[12] = (unsigned char)(1);
    infoHeader[14] = (unsigned char)(bytesPerPixel*8);

    return infoHeader;
}
