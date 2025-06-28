dofile("scripts/conversion.lua")
dofile("scripts/math.lua")
dofile("scripts/music.lua")
dofile("scripts/timer.lua")

local genCode = table.concat({...}, " ")
local chunk, e = load(genCode)
if chunk then
    chunk()
else
    print("Error loading generated code:", e)
end