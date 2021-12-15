def mean_confidence_interval(data, alpha):
  n = len(data)
  m = float(sum(data))/n # sample mean
  var = sum([(x - m)**2 for x in data]) / float(n-1) # sample variance
  # calls the inverse CDF of the Student's t distribution
  import scipy.stats, math
  tfact = scipy.stats.t._ppf(1-alpha/2., n-1)
  h = tfact * math.sqrt(var/n)
  return m-h, m+h
if __name__ == "__main__":
  confidence = .99 # 95%
  alpha = 1 - confidence
  data = [2268,2505,2414,2393,2327.5,2495,2425.5,2594.5,2467,2490,2430,2395.5,2487.5,2546.5,2626.5,2119,2533,2312.5,2368,2303.5,2358.5,2363.5,2417.5,2432.5,2416.5,2401,2264.5,2504,2262,2381.5,2414,2532,2344.5,2513,2420.5,2476,2388.5,2327.5,2469,2479,2485,2415.5,2393,2593.5,2589.5,2165,2399.5,2518.5,2361.5,2372,2479.5,2256,2453,2307,2339.5,2509,2142,2300.5,2609,2486,2664,2375,2458.5,2282.5,2430,2541.5,2370,2343,2432.5,2439,2257,2311,2380.5,2453,2424.5,2429.5,2315.5,2494,2519,2423.5,2316,2387,2297,2460,2332.5,2389,2533.5,2302,2546,2384,2450.5,2466.5,2470.5,2361,2312.5,2461,2374,2420,2444.5,2519.5,2219,2313.5,2527,2510,2430,2401.5,2545,2483,2388.5,2513,2494,2570.5,2400.5,2562,2277,2556,2535,2505.5,2376,2321,2417.5,2343.5,2410,2526,2319,2434.5,2512.5,2269.5,2345,2433.5,2355,2545,2189,2478.5,2519,2383.5,2382.5,2454,2486.5,2460,2587,2508.5,2484.5,2280.5,2417.5,2474.5,2278,2419.5,2496.5,2417,2188,2565,2539,2393.5,2355.5,2533.5,2301.5,2357.5,2548,2437.5,2470,2444.5,2382.5,2410.5,2498,2430,2442.5,2473,2427,2346.5,2314.5,2270.5,2532.5,2266.5,2294.5,2303,2310.5,2519,2361,2437.5,2436.5,2319.5,2507.5,2598,2371,2401,2276.5,2439.5,2559,2574.5,2500,2620.5,2459,2232.5,2304,2419.5,2399.5,2506.5,2339.5,2401,2485,2310,2554.5,2563.5,2274,2374,2451,2366.5,2338.5,2474,2229,2534.5,2536,2140.5,2086.5,2503.5,2414,2270.5,2436.5,2250,2316,2409,2462,2423.5,2437.5,2571,2521,2280,2280.5,2539.5,2416.5,2307,2368,2345.5,2338.5,2544,2394,2579,2453,2484,2262,2511.5,2439.5,2429,2555.5,2456,2432.5,2456,2502.5,2466.5,2375,2295.5,2384.5,2305.5,2371.5,2375,2307.5,2459.5,2368,2386,2446.5,2284,2397,2362.5,2412.5,2197,2334.5,2507.5,2394.5,2631.5,2449.5,2495,2465,2542,2481.5,2325.5,2299.5,2362,2286.5,2480,2242.5,2533.5,2370.5,2354,2518.5,2452.5,2315.5,2286.5,2353.5,2282.5,2428.5,2422.5,2453,2657,2354,2369.5,2337.5,2214,2447.5,2395,2369,2445,2515,2252,2654.5,2407.5,2525,2341,2497.5,2404,2281.5,2207.5,2397.5,2415.5,2367.5,2541.5,2246,2223,2520,2463.5,2386.5,2395.5,2435.5,2408.5,2419,2512,2537,2533.5,2383.5,2436,2493.5,2314.5,2456,2472.5,2225.5,2403,2442.5,2439.5,2316,2213.5,2450,2280,2482,2390,2480,2357,2485,2412,2519,2550,2447.5,2399,2410.5,2424.5,2348,2473.5,2320.5,2283.5,2425.5,2311,2303,2416.5,2452.5,2409,2318.5,2380.5,2494,2447.5,2655.5,2433.5,2384.5,2422,2335.5,2425.5,2450.5,2486,2598.5,2381.5,2371.5,2426,2338.5,2509.5,2396.5,2420,2362,2341,2369,2391,2292.5,2195,2453,2452,2589.5,2315.5,2547,2431.5,2376.5,2214.5,2338.5,2346.5,2527.5,2586.5,2330,2327.5,2378.5,2347,2448,2269.5,2271,2251.5,2361.5,2349,2616,2584.5,2397.5,2145,2297,2324.5,2417,2364.5,2523,2269.5,2443,2208.5,2432.5,2181,2254,2521.5,2551.5,2419.5,2331,2320,2487.5,2344,2411,2314.5,2441.5,2401,2541,2521.5,2425,2375,2534.5,2419.5,2330,2590.5,2258.5,2250.5,2212,2512,2363.5,2430.5,2495.5,2415,2432,2525,2467.5,2404,2374,2628.5,2489,2560,2329.5,2421.5,2326,2442,2406.5,2518,2427.5,2420.5,2337.5,2506,2369,2392,2394,2465.5,2532.5,2301,2479.5,2311.5,2249,2436,2427,2473,2392,2525.5,2542,2476,2356,2443.5,2236.5,2325.5,2602,2462,2390.5,2479,2354.5,2503,2552.5,2475.5,2365,2453,2387.5,2366,2312,2361,2484,2477,2326.5,2600.5,2295,2391,2591,2403,2372.5,2337.5,2172.5,2414,2285,2455.5,2417,2297,2386,2466,2562.5,2448.5,2411,2381,2296,2303,2370.5,2283.5,2366,2411,2477,2403.5,2328.5,2354,2460,2315.5,2252,2497.5,2505,2795,2373,2580.5,2321,2489.5,2434.5,2402,2514.5,2318.5,2509.5,2483.5,2428.5,2566,2346.5,2332.5,2509,2305.5,2416.5,2217,2361.5,2319.5,2461.5,2465.5,2392.5,2438.5,2358.5,2457,2520.5,2367,2373.5,2225.5,2473.5,2428,2503.5,2476,2584.5,2518.5,2489,2301.5,2518,2471.5,2204,2417,2552.5,2579,2324,2388,2428,2578,2372,2430.5,2477,2473,2456.5,2434.5,2366.5,2593,2378.5,2488.5,2405,2532,2394,2302,2261,2401,2158,2262.5,2489,2480.5,2457,2348.5,2271.5,2514.5,2245,2402,2209.5,2463,2264.5,2463,2352,2458,2311.5,2447,2590.5,2242,2491,2410.5,2378,2341.5,2392,2442.5,2383,2440.5,2403.5,2283,2419.5,2600,2431,2256,2287,2313,2452.5,2499,2470,2336.5,2358,2505.5,2439,2271,2351.5,2277.5,2317.5,2440,2405,2402,2441.5,2424,2308.5,2573.5,2174,2480.5,2220.5,2461.5,2387.5,2319,2566,2443.5,2278,2491,2319.5,2450,2442,2361,2379,2271,2415,2397,2511,2399,2401,2400.5,2406.5,2395.5,2302.5,2275.5,2414,2483,2408,2333,2490.5,2434.5,2439,2417,2506.5,2526.5,2380.5,2516,2438,2567,2215.5,2407.5,2400.5,2334.5,2346.5,2376,2349,2641.5,2300,2491,2513.5,2432.5,2321.5,2420,2392.5,2239.5,2462,2212.5,2509,2522.5,2380,2388,2256,2534.5,2359.5,2503,2317.5,2442.5,2362.5,2459.5,2548,2456,2309.5,2292.5,2452.5,2499,2468,2344.5,2328,2569.5,2399.5,2348,2229.5,2449,2517,2270,2383,2277,2477.5,2388.5,2470.5,2510.5,2486.5,2374,2504,2384.5,2539.5,2412.5,2399.5,2499,2467,2497,2334.5,2400.5,2492,2220,2427.5,2348.5,2498,2383.5,2356,2385.5,2465,2312,2454.5,2313,2279,2586.5,2298.5,2359,2489,2313.5,2443.5,2373.5,2435.5,2540.5,2571.5,2442,2415.5,2544.5,2445,2407.5,2442,2303.5,2301.5,2586.5,2522,2462,2363,2602.5,2264,2473.5,2403,2422.5,2508.5,2366,2464.5,2444,2420.5,2443,2437,2483.5,2506,2505.5,2436,2658.5,2404.5,2491,2346,2379.5,2452,2366,2466.5,2314,2412,2313,2380,2330,2420.5,2431.5,2260.5,2498,2566,2510,2512,2452.5,2368.5,2239.5,2408.5,2553.5,2423.5,2313,2383.5,2290,2471.5,2384.5,2388.5,2321,2345,2335.5,2249.5,2361,2430,2417.5,2335.5,2418,2360,2417.5,2519,2542,2344.5,2340,2300.5,2512,2459,2511.5,2321.5,2466,2483,2450,2394.5,2254,2409,2409.5,2437,2160,2327.5,2357.5,2520,2391,2406.5,2440.5,2820,2366,2488,2554,2455.5,2579.5,2330,2442,2588,2322.5,2224,2514,2484.5,2460,2483.5,2397.5,2271,2371.5,2404,2465.5,2513.5,2397,2384.5,2331,2386,2421.5,2385,2354.5,2307.5,2362.5,2162.5,2492,2421,2459.5,2539.5,2365.5,2519.5,2283,2457,2418,2482,2580,2426,2455.5,2351,2387,2212,2313,2436,2694,2346,2339.5,2423.5,2407,2383.5,2246,2305,2495.5,2503.5,2419.5,2483.5,2383,2399,2280.5,2386,2305,2299.5,2364,2416.5,2293.5,2526.5,2467,2448,2403.5,2443.5,2515,2467.5,2519.5,2427,2326,2460.5,2237.5,2389.5,2246,2498.5,2204.5,2368.5,2405.5,2371.5,2380.5,2413,2291.5,2221,2403.5,2247.5,2386.5,2370,2326,2393.5,2406,2354.5,2130.5,2576,2499.5,2452.5,2502,2486,2344,2421,2192,2337.5,2384,2482.5,2360,2423,2464.5]
  print(mean_confidence_interval(data, alpha))