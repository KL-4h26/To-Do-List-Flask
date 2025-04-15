document.addEventListener('DOMContentLoaded', function() {
    // Восстановление состояния секций из localStorage
    const sectionsState = JSON.parse(localStorage.getItem('sectionsState')) || {
        'active-tasks': false,
        'completed-tasks': false
    };

    // Инициализация состояния секций
    function initSections() {
        Object.keys(sectionsState).forEach(sectionId => {
            const section = document.getElementById(sectionId);
            const icon = document.querySelector(`[data-section="${sectionId}"] .toggle-icon`);

            if (sectionsState[sectionId]) {
                section.classList.add('collapsed');
                icon.classList.remove('fa-chevron-down');
                icon.classList.add('fa-chevron-up');
            }
        });
    }

    // Переключение состояния секции
    function toggleSection(sectionId) {
        const section = document.getElementById(sectionId);
        const icon = document.querySelector(`[data-section="${sectionId}"] .toggle-icon`);

        // Переключаем состояние
        sectionsState[sectionId] = !sectionsState[sectionId];

        // Применяем изменения
        section.classList.toggle('collapsed');
        icon.classList.toggle('fa-chevron-down');
        icon.classList.toggle('fa-chevron-up');

        // Сохраняем состояние
        localStorage.setItem('sectionsState', JSON.stringify(sectionsState));
    }

    // Назначение обработчиков событий
    function setupEventListeners() {
        document.querySelectorAll('.section-header').forEach(header => {
            header.addEventListener('click', function() {
                toggleSection(this.dataset.section);
            });
        });
    }

    // Инициализация
    initSections();
    setupEventListeners();
});