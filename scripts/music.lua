function fileExists(pth)
    local f = io.open(pth, "r")
    if f then f:close() return true else return false end
end


function play(query)
    -- just change it for now
    local dlpPath = 'yt-dlp'
    local handle = io.popen(dlpPath.." --get-id --quiet 'ytsearch:" .. query .. "'")
    local vidId = handle:read("*l")
    handle:close()

    os.execute("pkill mpv")
    -- just wait until it dies so no race condition happens
    while os.execute("pgrep mpv > /dev/null") == 0 do end
    os.execute(string.format(
        "mpv --no-video https://youtube.com/watch?v=%s", vidId
    ))
end

