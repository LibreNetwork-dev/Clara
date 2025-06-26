function fileExists(pth)
    local f = io.open(pth, "r")
    if f then f:close() return true else return false end
end


function play(query)
    local dlpPath = '../bin/yt-dlp'
    local handle = io.popen(dlpPath.." --get-id --quiet 'ytsearch:" .. query .. "'")
    local vidId = handle:read("*l")
    handle:close()

    local cachePath = "./cache/music/" .. vidId .. ".mp4"
    os.execute("pkill mpv")
    while os.execute("pgrep mpv > /dev/null") == 0 do end
    if fileExists(cachePath) then
        local res = os.execute("mpv --no-video '" .. cachePath .. "'") 
        if (res ~= 0) then
            -- re dl if the file is malformed
            os.execute(string.format(
                "%s -f bestaudio -o - https://youtube.com/watch?v=%s | tee '%s' | mpv --no-video -",
                dlpPath, vidId, cachePath
            ))
        end
    else --cache & play at the same time so its fasttttt
        os.execute(string.format(
            "%s -f bestaudio -o - https://youtube.com/watch?v=%s | tee '%s' | mpv --no-video -",
            dlpPath, vidId, cachePath
        ))
    end
end

