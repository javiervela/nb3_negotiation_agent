package commodityMarket.improvedAgent;

import java.net.InetAddress;
import java.net.UnknownHostException;

import commodityMarket.domain.CommodityAssets;
import commodityMarket.domain.CommodityMarket;
import commodityMarket.domain.CommodityUtilityProfile;
import ddejonge.negoServer.Logger;

public class RunMarketAndFiveAgents {

	public enum ConcessionPreset {
		GREEDY(-4, -4),
		LAZY(4, -4),
		PICKY(-4, 4),
		DESPERATE(4, 4),
		DEFAULT(2, 4),
		NEUTRAL(1, 1);

		private final int alpha1;
		private final int alpha2;

		ConcessionPreset(int alpha1, int alpha2) {
			this.alpha1 = alpha1;
			this.alpha2 = alpha2;
		}

		public int getAlpha1() {
			return alpha1;
		}

		public int getAlpha2() {
			return alpha2;
		}
	}

	/**
	 * Starts 5 negotiators, each in a new thread.
	 * 
	 * @param args
	 */
	public static void main(String[] args) {

		String[] names = { "Alice", "Bob", "Charles", "David", "Eve" };

		// If this method is called on 23 December 2015 at exactly 15:50
		// then the dateString will be: 2015_12_23__15-30-00
		String dateString = Logger.getDateString();

		// Set the path where all the log files will be stored.
		String logfolderPath = "log/" + dateString;

		// Set the duration of the negotiations to 30 seconds.
		int negotiationLength = 30 * 1000;

		// Run an instance of the Commodity Market
		CommodityMarket market = new CommodityMarket(logfolderPath, negotiationLength);
		CommodityAssets assets = CommodityAssets.getRandomInstance();
		market.setAssets(assets);
		CommodityUtilityProfile utilityProfile = CommodityUtilityProfile.getRandomProfile(assets.NUM_AGENTS,
				assets.NUM_COMMODITIES);
		market.setUtilityProfile(utilityProfile);
		market.start();

		try {

			InetAddress serverAddress = InetAddress.getLocalHost();

			ConcessionPreset[] presets = {
					ConcessionPreset.GREEDY,
					ConcessionPreset.LAZY,
					ConcessionPreset.PICKY,
					ConcessionPreset.DESPERATE,
					ConcessionPreset.DEFAULT
			};

			for (int i = 0; i < 5; i++) {

				System.out.println("RunFiveAgents.main() starting agent " + names[i]);

				ImprovedNegotiator agent = new ImprovedNegotiator(names[i], serverAddress, 1234, presets[i].getAlpha1(),
						presets[i].getAlpha2());
				agent.enableLoggers(logfolderPath);
				agent.start();
			}

		} catch (UnknownHostException e) {
			e.printStackTrace();
		}

	}

}
