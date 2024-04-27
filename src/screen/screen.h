#ifndef SCREEN_H
#define SCREEN_H

#include "ili9341.h"

#define SIZE (ILI9341_TFTHEIGHT*ILI9341_TFTWIDTH)

class Screen{
    private:
        uint16_t height;
        uint16_t width;
        uint16_t screen_buffer[SIZE];

        void PlotCirclePoints(uint16_t xc, uint16_t yc, uint16_t x, uint16_t y, uint16_t color);

    public:
        Screen();
        ~Screen();
        uint16_t GetWidth();
        uint16_t GetHeight();
        void ClearScreen(uint16_t color=0);
        void DrawLine(uint16_t x1, uint16_t y1, uint16_t x2, uint16_t y2, uint16_t color=0xffff);
        void DrawCircle(uint16_t xc, uint16_t yc, uint16_t radius, uint16_t color=0xffff, bool fill=true);
        void DrawRectangle(uint16_t start_x, uint16_t start_y, uint16_t end_x, uint16_t end_y, uint16_t color=0xffff, bool fill=true);
        void DrawImage(uint16_t x, uint16_t y/*image*/);
        void Render();
};

uint16_t ConvertColor565(uint8_t r, uint8_t g, uint8_t b);

#endif