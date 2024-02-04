import Foundation

@available(macOS 12, iOS 15, watchOS 8, tvOS 15, *)
func fetchURL(_ url: URL) async throws -> (Data, URLResponse) {
    
    var urlRequest = URLRequest(url: url)
    urlRequest.setValue("application/vnd.github.v3+json", forHTTPHeaderField: "Accept")

    let (data, response) = try await URLSession.shared.data(from: url)
    return (data, response)
}

@available(macOS 12, iOS 15, watchOS 8, tvOS 15, *)
func main() async {
    let frontendURL = URL(string: "https://api.github.com/repos/DevOps-2023-TeamA/tsao-frontend-svc/pulls?state=closed&sort=updated&direction=desc")!
    
    do {
        let (data, _) = try await fetchURL(frontendURL)
        if let jsonString = String(data: data, encoding: .utf8) {
            print(jsonString)
        }
    } catch {
        print("Request failed with error: \(error)")
    }
}

// Run the async function
if #available(macOS 12, iOS 15, watchOS 8, tvOS 15, *) {
    Task {
        await main()
    }
} else {
    print("Async/Await is not supported on this platform.")
}

RunLoop.current.run(until: Date().addingTimeInterval(20))
