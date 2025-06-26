function calc(expr)
    local env = {
        math = math,
        abs = math.abs, sin = math.sin, cos = math.cos,
        pi = math.pi, sqrt = math.sqrt,
        log = math.log, exp = math.exp,
    }
    local f, err = load("return " .. expr, "expr", "t", env)
    if not f then return nil, "Parse error: " .. err end
    local ok, result = pcall(f)
    if not ok then return nil, "Runtime error: " .. result end
    return result
end
