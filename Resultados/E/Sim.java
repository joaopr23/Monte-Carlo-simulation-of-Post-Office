import java.util.*;
import java.text.DecimalFormat;
import java.math.RoundingMode;
import java.text.DecimalFormatSymbols;

class Packet {
    int modality; //1 for Home delivery, 0 for locker pick-up
    int marked;

    public Packet(int modality){
      this.modality = modality;
      marked=0;
    }
}

class Locker {
    ArrayList<Packet> Lpackets;
    Double TotalCost;
    int maxItems;
    int TotalPF=0;
    int TotalOC=0;
    int TotalLCKR=0;
    Double[][] mStats2 = new Double[120][2];
    int[][] mStats1 = new int [120][5];

    public Locker () {
      Lpackets = new ArrayList<Packet>();
      TotalCost = Double.valueOf(0);
      maxItems=0;
      for(int i = 0 ; i < 120; i++){
        for(int j = 0 ; j < 5 ; j++){
          mStats1[i][j]=0;
        }
      }

      for(int i = 0 ; i < 120 ; i++)
        for(int j = 0 ; j < 2 ; j++)
          mStats2[i][j]=Double.valueOf(0);
        }
      }

public class Sim {

  private static void PForders (Locker myLocker, int iteration){

    int PFcounter = 0;
    int index = 0;
    int conta = 0;

    while(myLocker.Lpackets.size() > index){
      Packet packet = myLocker.Lpackets.get(index);
      if(packet.modality==1){
        PFcounter++;
        myLocker.mStats1[iteration][2]++;
        myLocker.TotalPF++;
        myLocker.Lpackets.remove(index);
      }
      else{
        index++;
      }
    }
    if(PFcounter<=10){
      myLocker.TotalCost+= Double.valueOf(PFcounter);
      myLocker.mStats2[iteration][0]+=Double.valueOf(PFcounter);
    }
    if(PFcounter>10){
      myLocker.TotalCost=myLocker.TotalCost + Double.valueOf(2*(PFcounter-10)+10);
      myLocker.mStats2[iteration][0]+=Double.valueOf(2*(PFcounter-10)+10);
    }
     PFcounter = 0;
  }

  private static void arrivals (Locker myLocker, int iteration){
    Random rand = new Random();
    int newOrders = rand.nextInt(50 - 10 + 1) + 10;
      for(int i = 0 ; i < newOrders ; i++){
        if(rand.nextDouble()< 0.50){
            Packet packet1 = new Packet(0);
            myLocker.Lpackets.add(packet1);
            myLocker.mStats1[iteration][0]++;
        }
        else {
          Packet packet2 = new Packet(1);
          myLocker.Lpackets.add(packet2);
          myLocker.mStats1[iteration][1]++;
        }
      }
  }

  private static void OCs (Locker myLocker, int iteration, Double probability, Double compensation){
    Random rand = new Random();
    int index=0;
    int index1=0;

    while(myLocker.Lpackets.size() > index){
      Packet packet = myLocker.Lpackets.get(index);
      if (packet.modality==0){
        if (rand.nextDouble() < 0.75) { // <-- 75% of the time.
          myLocker.Lpackets.remove(index);
          myLocker.mStats1[iteration][4]++;
          myLocker.TotalLCKR++;

          if(rand.nextDouble()< probability) {
            index1=0;
            while(myLocker.Lpackets.size() > index1){

              Packet packet1 = myLocker.Lpackets.get(index1);
              if(packet1.modality==1&&packet1.marked==0){
                packet1.marked=1;
                myLocker.mStats1[iteration][3]++;
                myLocker.TotalOC++;

                myLocker.TotalCost=myLocker.TotalCost+Double.valueOf(compensation);
                myLocker.mStats2[iteration][1]+=Double.valueOf(compensation);
                break;
              }
            index1++;
            }
          }
        }
        else index++;
      }
      else index++;
    }
        int index4=0;
        while(myLocker.Lpackets.size() > index4){
          Packet packet1 = myLocker.Lpackets.get(index4);
          if(packet1.modality==1&&packet1.marked==1){
          myLocker.Lpackets.remove(index4);}
          else {index4 ++;};
    }
  }

  private static void printStats (Locker myLocker, int iteration){

    DecimalFormatSymbols otherSymbols = new DecimalFormatSymbols(Locale.GERMAN);
    otherSymbols.setDecimalSeparator('.');
    otherSymbols.setGroupingSeparator('\0');
    DecimalFormat df = new DecimalFormat("#.#", otherSymbols);

    String leftAlignFormat = "| %-7s ";
    int counter0=0;
    int counter1=0;
    int index=0;
    while(myLocker.Lpackets.size() > index){
      Packet packet = myLocker.Lpackets.get(index);
      if(packet.modality==1){
        counter1++;
      }
      else {
        counter0++;
      }
        index++;
    }
    System.out.format(leftAlignFormat, (iteration+1));
    System.out.format(leftAlignFormat, myLocker.mStats1[iteration][1]);
    leftAlignFormat = " %-5s ";
    System.out.format(leftAlignFormat, myLocker.mStats1[iteration][0]);
    leftAlignFormat = "| %-2s ";
    System.out.format(leftAlignFormat, myLocker.mStats1[iteration][2]);
    leftAlignFormat = " %-2s ";
    System.out.format(leftAlignFormat, myLocker.mStats1[iteration][3]);
    leftAlignFormat = " %-3s ";
    System.out.format(leftAlignFormat, myLocker.mStats1[iteration][4]);
    leftAlignFormat = "| %-6s ";
    System.out.format(leftAlignFormat, myLocker.TotalPF);
    leftAlignFormat = " %-9s ";
    System.out.format(leftAlignFormat, myLocker.TotalOC);
    leftAlignFormat = " %-4s ";
    System.out.format(leftAlignFormat, myLocker.TotalLCKR);
    leftAlignFormat = "| %-5s ";
    System.out.format(leftAlignFormat,df.format(myLocker.mStats2[iteration][0]));
    leftAlignFormat = " %-7s ";
    System.out.format(leftAlignFormat,df.format(myLocker.mStats2[iteration][1]));
    leftAlignFormat = " %-8s ";
    System.out.format(leftAlignFormat,df.format(myLocker.TotalCost));
    leftAlignFormat = "| %-5s ";
    System.out.format(leftAlignFormat,counter1);
    leftAlignFormat = " %-5s ";
    System.out.format(leftAlignFormat,counter0);
    System.out.format(leftAlignFormat,"|");
    System.out.print("\n");
  }

  private static void updateLocker(Locker myLocker, int iteration, Double probability, Double compensation){

    OCs(myLocker, iteration, probability, compensation);
    PForders(myLocker, iteration);
    arrivals(myLocker, iteration);
    if(myLocker.Lpackets.size() > myLocker.maxItems){
      myLocker.maxItems=myLocker.Lpackets.size();
    }
  }

  public static void main (String[] args){
    Double probability = 0.75;
    Double compensation = 1.8;
    Double CostsArray[] = new Double[1000];
    int maxItemsArray[] = new int[1000];

    for(int j = 0 ; j < 1000 ; j++){
      Double TotalCost = Double.valueOf(0);
      Locker myLocker = new Locker();
      String leftAlignFormat = "| %-15s | %-4d |%n";

      System.out.format("+---------+----------------+-------------+-------------------------+--------------------------+---------------+%n");
      System.out.format("| Day     | NEW PACKAGES   |  DELIVERIES | ACCUMULATED  DELIVERIES |          COSTS           | LOCKER STATUS | %n");
      System.out.format("+---------+----------------+-------------+-------------------------+--------------------------+---------------+%n");
      System.out.format("| t       | home    lckr   | pf  oc lckr |    pf     oc     lckr   |   pf       oc      ACC   |  home   lckr  |%n");
      System.out.format("+---------+----------------+-------------+-------------------------+--------------------------+---------------+%n");
      for(int i = 0 ; i < 120 ; i++) {
        updateLocker(myLocker,i, probability, compensation);
        printStats(myLocker,i);
      }
      System.out.format("+---------+----------------+-------------+-------------------------+--------------------------+---------------+%n");

      CostsArray[j]=myLocker.TotalCost;
      maxItemsArray[j]=myLocker.maxItems;
    }

    DecimalFormatSymbols otherSymbols = new DecimalFormatSymbols(Locale.GERMAN);
    otherSymbols.setDecimalSeparator('.');
    otherSymbols.setGroupingSeparator('\0');
    DecimalFormat df = new DecimalFormat("#.#", otherSymbols);

    System.out.print("\n");
    System.out.println("Custos Totais:");
    System.out.print("[");
    for(int i = 0 ; i < 1000 ; i++){
      if(i!=0){
        System.out.print("," + df.format(CostsArray[i]));
      }
      else{
        System.out.print( df.format(CostsArray[i]));
      }
    }
    System.out.print("]");
    System.out.print("\n\n");
    System.out.println("Número máximo de itens:");
    System.out.print("[");
    for(int i = 0 ;  i < 1000 ; i++){
      if(i!=0){
        System.out.print("," + maxItemsArray[i]);
      }
      else {
        System.out.print(maxItemsArray[i]);
      }
    }
    System.out.print("]");
  }
}
