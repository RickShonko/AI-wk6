def performance_comparison():
    """Compare Cloud AI vs Edge AI performance"""
    
    comparison_data = {
        "Metric": ["Latency", "Bandwidth Usage", "Privacy", "Offline Operation", "Cost per 1M inferences"],
        "Cloud AI": ["200-500ms", "High", "Data in cloud", "Not possible", "$50-100"],
        "Edge AI": ["20-50ms", "Low", "Data local", "Fully supported", "$5-10"],
        "Advantage": ["10x faster", "80% reduction", "Enhanced", "Always available", "80% cheaper"]
    }
    
    print("\n" + "="*60)
    print("CLOUD AI vs EDGE AI PERFORMANCE COMPARISON")
    print("="*60)
    
    for i in range(len(comparison_data["Metric"])):
        metric = comparison_data["Metric"][i]
        cloud = comparison_data["Cloud AI"][i]
        edge = comparison_data["Edge AI"][i]
        advantage = comparison_data["Advantage"][i]
        
        print(f"\n{metric}:")
        print(f"  ☁️  Cloud AI: {cloud}")
        print(f"  📱 Edge AI: {edge}")
        print(f"  ✅ Advantage: {advantage}")

performance_comparison()