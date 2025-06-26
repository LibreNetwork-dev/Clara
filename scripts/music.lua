function fileExists(pth)
    local f = io.open(pth, "r")
        if f then
        f:close()
            return true
        else 
            return false
        end 
end

function play(query) 
    local dlpPath = '../bin/yt-dlp'
    local handle = io.popen("yt-dlp --get-id --continue 'ytsearch:" .. query .. "'")
    local vidId = handle:read("*l")
    handle:close()

    if fileExists('../cache/music/'..vidId) then 
        os.execute("mpv --no-video ../cache/music/"..vidId..".mp4")
        return 0;
    else  
        os.execute(dlpPath.." -o ../cache/music/'"..vidId..".mp4'".." --continue --merge-output-format mp4 https://youtube.com/watch?v="..vidId )
        os.execute("mpv --no-video ../cache/music/"..vidId..".mp4")    
    end
end

-- for testing ok ill impl it soon (probably)
play("highway to hell")