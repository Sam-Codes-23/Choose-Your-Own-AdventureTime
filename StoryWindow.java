import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.plaf.DimensionUIResource;

public class Storywindow {

	public static void main(String[] args) {
		JPanel panel = new JPanel();
		JFrame frame = new JFrame();

		frame.setSize(900, 750);

		frame.setPreferredSize(new DimensionUIResource(0, 0));
		frame.setMaximumSize(new DimensionUIResource(0, 0));
		frame.setMinimumSize(new DimensionUIResource(0, 0));
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setResizable(false);
		frame.add(panel);
		
		panel.setLayout(null);
		
		JLabel userLable = new JLabel("Main Title");
		userLable.setBounds(400, 20, 195, 25);
		panel.add(userLable);
		
		JButton button0 = new JButton("Story 1");
		button0.setBounds(240, 490, 150, 25);
		panel.add(button0);
		
		JButton button1 = new JButton("Story 3");
		button1.setBounds(240, 550, 150, 25);
		panel.add(button1);
		
		JButton button2 = new JButton("Story 2");
		button2.setBounds(520, 490, 150, 25);
		panel.add(button2);
		
		JButton button3 = new JButton("Story 4");
		button3.setBounds(520, 550, 150, 25);
		panel.add(button3);

		
		frame.setVisible(true);

	}
	public void actionPerformed(ActionEvent e) {
			
    }

}
