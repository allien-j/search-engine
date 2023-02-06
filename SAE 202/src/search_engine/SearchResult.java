package search_engine;

public class SearchResult {
	private String url;
	private double score;

	public SearchResult(String url, double score) {
		super();
		this.url = url;
		this.score = score;
	}

	public String getUrl() {
		return url;
	}

	public double getScore() {
		return score;
	}

	public String toString() {
		return "SearchResult [url=" + url + ", score=" + score + "]";
	}
	
	
}
