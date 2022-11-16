
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.plaf.DimensionUIResource;

import java.awt.event.ActionEvent;

public class Mainwindow{
    
        public static void main(String [] args) {
            JPanel panel = new JPanel();
            JFrame frame = new JFrame();
            frame.setSize(900,750);
			      frame.setPreferredSize(new DimensionUIResource(0, 0));
			      frame.setMaximumSize(new DimensionUIResource(0, 0));
			      frame.setMinimumSize(new DimensionUIResource(0, 0));
			      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			      frame.setResizable(false);

            frame.add(panel);
    
            panel.setLayout(null);
            
            JLabel userLable = new JLabel("Pause");
                userLable.setBounds(420, 20, 165, 25);
                panel.add(userLable);
                
            JButton button = new JButton("New Adventure");
                button.setBounds(380, 440, 150, 25); 
                panel.add(button);
                
            JButton button2 = new JButton("Exit");
                button2.setBounds(380, 480, 150, 25);
                panel.add(button2);
                
    
            frame.setVisible(true);
    
        }
        public void actionPerformed(ActionEvent e) {
                
        }
    
    
    }

