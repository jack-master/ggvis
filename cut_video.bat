@echo off
set /p input_video_path=请把视频拖进来：
set /p start_time=请输入开始时间(英文字符hh:mm:ss)：
set /p end_time=请输入结束时间(英文字符hh:mm:ss)：
set /p new_name=请输入新名称，若为空，则变成“cut_原名”：

for %%I in ("%input_video_path%") do (
    set "extension=%%~xI"
    set "parent_folder=%%~dpI"
    set "original_name=%%~nI"
)

if "%new_name%"=="" (
    set "new_name=cut_%original_name%"
)

ffmpeg -i "%input_video_path%" -ss %start_time% -to %end_time% -c copy "%parent_folder%%new_name%%extension%" >nul 2>&1

echo 视频裁剪完成！
pause