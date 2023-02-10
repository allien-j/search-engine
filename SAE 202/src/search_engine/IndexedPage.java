package search_engine;

import java.util.Arrays;

public class IndexedPage {
	private String url;
	private String[] words;
	private int counts;
	
	public IndexedPage(String[] lines) {
		super();
		this.url = lines[0];
		for(int i=1; i<lines.length;i++) {
			this.words[i-1] = lines[i]; 
		}
	}

	public IndexedPage(String text) {//Surement faux ressemble plus à getCount()
		super();
		Arrays.sort(this.words);
		for(int i=0;i<this.words.length;i++) {
			String[] currentWord = this.words.split(":");//String.split pas l'air de fonctionner à rechercher plus tard
			if(currentWord[1] == text) {
				this.counts++;
			}
		}
	}

	public String getUrl() {
		return url;
	}

	
	
	

}
