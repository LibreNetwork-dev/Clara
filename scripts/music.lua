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

    if fileExists(cachePath) then
        os.execute("mpv --no-video '" .. cachePath .. "'") 
    else --cache & play at the same time so its fasttttt
        os.execute(string.format(
            "%s -f bestaudio -o - https://youtube.com/watch?v=%s | tee '%s' | mpv --no-video -",
            dlpPath, vidId, cachePath
        ))
    end
end

