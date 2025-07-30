from urllib.parse import urlparse

def analyze_url(url):
    """Analisa uma URL em busca de indicadores de phishing"""
    suspicious_keywords = [
        'login', 'account', 'verify', 'secure', 'bank', 
        'update', 'payment', 'confirm', 'click'
    ]
    
    # Extrai o domínio principal
    domain = urlparse(url).netloc.lower()
    
    # Verifica características suspeitas
    warnings = []
    if not url.startswith('https://'):
        warnings.append("❌ Usa HTTP inseguro (sem HTTPS)")
    if any(keyword in domain or keyword in url.lower() for keyword in suspicious_keywords):
        warnings.append(f"⚠️ Contém palavras suspeitas: {', '.join(suspicious_keywords)}")
    if '-' in domain or len(domain.split('.')) > 3:
        warnings.append("⚠️ Domínio incomum (pode ser falsificado)")
    
    return warnings if warnings else ["✅ URL parece segura"]

if __name__ == "__main__":
    print("=== Detector de URLs Suspeitas ===")
    while True:
        url = input("\nDigite a URL (ou 'sair'): ")
        if url.lower() == 'sair':
            break
        
        results = analyze_url(url)
        print("\nResultados:")
        for msg in results:
            print(f"- {msg}")