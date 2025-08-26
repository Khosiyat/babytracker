const FeedingForm: React.FC = () => {
    const [foodItems, setFoodItems] = useState([]);
    const [amount, setAmount] = useState('');
    const [foodId, setFoodId] = useState('');
  
    const babyId = parseInt(localStorage.getItem('babyId') || '1');
    const caregiverId = parseInt(localStorage.getItem('userId') || '1');
  
    useEffect(() => {
      fetchFoodItems().then(res => setFoodItems(res.data));
    }, []);
  
    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault();
      await logFeeding({
        baby: babyId,
        caregiver: caregiverId,
        food_item: foodId,
        amount_ml: parseFloat(amount),
      });
      alert('Feeding logged!');
      setAmount('');
    };
  
    ...
  };
  
  
    ...
  };
  